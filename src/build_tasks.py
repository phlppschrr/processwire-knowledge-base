#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class SearchIndex:
    classes: dict[str, str]
    methods: dict[tuple[str, str], str]


@dataclass
class HookIndex:
    hookable: set[tuple[str, str]]


def load_search_index(path: Path) -> SearchIndex:
    data = json.loads(path.read_text(encoding="utf-8"))
    classes: dict[str, str] = {}
    methods: dict[tuple[str, str], str] = {}
    for item in data.get("items", []):
        if item.get("type") == "class":
            classes[item.get("name")] = item.get("file")
        elif item.get("type") == "method":
            cls = item.get("class")
            name = item.get("name")
            file = item.get("file")
            if cls and name and file:
                methods[(cls, name)] = file
    return SearchIndex(classes=classes, methods=methods)


def load_hookable_index(path: Path) -> HookIndex:
    data = json.loads(path.read_text(encoding="utf-8"))
    hookable = set()
    # Support new dict structure or fallback to old list (though we just changed it)
    classes = data.get("classes", {})
    if not classes and "items" in data:
        # Fallback for old structure if needed
        for item in data["items"]:
            cls = item.get("class")
            name = item.get("name_public") or item.get("name")
            if cls and name:
                hookable.add((cls, name))
        return HookIndex(hookable=hookable)

    for cls_name, methods in classes.items():
        for method in methods:
            name = method.get("name")
            if name:
                hookable.add((cls_name, name))
    return HookIndex(hookable=hookable)


def resolve_class(
    name: str,
    core_index: SearchIndex,
    full_index: SearchIndex,
    prefer_full: bool = False,
) -> tuple[str | None, str | None]:
    if prefer_full:
        if name in full_index.classes:
            return "full", full_index.classes[name]
    if name in core_index.classes:
        return "core", core_index.classes[name]
    if name in full_index.classes:
        return "full", full_index.classes[name]
    return None, None


def resolve_method(
    cls: str,
    name: str,
    core_index: SearchIndex,
    full_index: SearchIndex,
    prefer_full: bool = False,
) -> tuple[str | None, str | None]:
    key = (cls, name)
    if prefer_full:
        if key in full_index.methods:
            return "full", full_index.methods[key]
    if key in core_index.methods:
        return "core", core_index.methods[key]
    if key in full_index.methods:
        return "full", full_index.methods[key]
    return None, None


def build_tasks_map(
    tasks_path: Path,
    core_index: SearchIndex,
    full_index: SearchIndex,
    core_hooks: HookIndex,
    full_hooks: HookIndex,
    out_path: Path,
) -> None:
    tasks_data = json.loads(tasks_path.read_text(encoding="utf-8"))
    tasks = tasks_data.get("tasks", [])
    out_items = []

    for task in tasks:
        prefer_full = task.get("profile") == "full"
        task_entry = {
            "id": task.get("id"),
            "title": task.get("title"),
            "summary": task.get("summary"),
            "keywords": task.get("keywords", []),
            "classes": [],
            "methods": [],
            "guides": task.get("guides", []),
        }

        for cls in task.get("classes", []):
            profile, file = resolve_class(cls, core_index, full_index, prefer_full=prefer_full)
            if not profile or not file:
                continue
            task_entry["classes"].append({"name": cls, "profile": profile, "file": file})

        for method in task.get("methods", []):
            if "::" not in method:
                continue
            cls, name = method.split("::", 1)
            profile, file = resolve_method(cls, name, core_index, full_index, prefer_full=prefer_full)
            if not profile or not file:
                continue
            hookable = (cls, name) in (full_hooks.hookable if profile == "full" else core_hooks.hookable)
            task_entry["methods"].append(
                {
                    "class": cls,
                    "name": name,
                    "profile": profile,
                    "file": file,
                    "hookable": hookable,
                }
            )

        out_items.append(task_entry)

    out_path.write_text(
        json.dumps({"tasks": out_items}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

def build_global_hookable(
    core_hookable: Path,
    full_hookable: Path,
    out_path: Path,
) -> None:
    def load_items(path):
        data = json.loads(path.read_text(encoding="utf-8"))
        # Handle both new and old structure if necessary, though we expect new
        return data.get("classes", {})

    core_classes = load_items(core_hookable)
    full_classes = load_items(full_hookable)
    
    merged: dict[str, list[dict]] = {}
    seen: set[tuple[str, str]] = set()

    # Helper to add methods
    def add_methods(classes_dict, profile):
        for cls_name, methods in classes_dict.items():
            if cls_name not in merged:
                merged[cls_name] = []
            
            for m in methods:
                method_name = m.get("name")
                if not method_name:
                    continue
                
                key = (cls_name, method_name)
                if key in seen:
                    continue
                
                seen.add(key)
                # entry = dict(m)
                # entry["profile"] = profile # Optional: Add profile? 
                # To save space, let's omit profile if not strictly needed.
                # But if we want to trace origin, we can add it.
                # Given user asked for optimization, omitting profile is better.
                merged[cls_name].append(m)

    # Add core first (usually preferred?)
    add_methods(core_classes, "core")
    # Add full (skip duplicates)
    add_methods(full_classes, "full")

    out_path.write_text(
        json.dumps({"classes": merged}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build tasks map and global hookable index")
    parser.add_argument("--core", default="docs/api-core", help="Core docs directory")
    parser.add_argument("--full", default="docs/api-full", help="Full docs directory")
    parser.add_argument("--tasks", default="tasks.json", help="Tasks config")
    parser.add_argument("--out", default="docs", help="Output directory")
    args = parser.parse_args()

    core_dir = Path(args.core)
    full_dir = Path(args.full)
    out_dir = Path(args.out)

    core_search = load_search_index(core_dir / "_search.json")
    full_search = load_search_index(full_dir / "_search.json")
    core_hooks = load_hookable_index(core_dir / "_hookable.json")
    full_hooks = load_hookable_index(full_dir / "_hookable.json")

    out_dir.mkdir(parents=True, exist_ok=True)
    build_tasks_map(Path(args.tasks), core_search, full_search, core_hooks, full_hooks, out_dir / "_tasks.json")
    build_global_hookable(core_dir / "_hookable.json", full_dir / "_hookable.json", out_dir / "_hookable.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
