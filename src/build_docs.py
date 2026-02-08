#!/usr/bin/env python3
import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DOCBLOCK_RE = re.compile(r"/\*\*(.*?)\*/", re.S)
CLASS_DEF_RE = re.compile(
    r"^[ \t]*(?:abstract\s+|final\s+)?(class|interface|trait)\s+([A-Za-z_][A-Za-z0-9_]*)",
    re.M,
)
CLASS_DECL_AT_RE = re.compile(
    r"(?:abstract\s+|final\s+)?(class|interface|trait)\s+([A-Za-z_][A-Za-z0-9_]*)"
)
FUNC_DECL_AT_RE = re.compile(
    r"(?:abstract\s+|final\s+)?(?:(?:public|protected|private)\s+)?(?:static\s+)?function\s+&?\s*([A-Za-z_][A-Za-z0-9_]*)\s*\("
)
CONST_DECL_AT_RE = re.compile(
    r"(?:(?:public|protected|private)\s+)?const\s+([A-Za-z_][A-Za-z0-9_]*)"
)

KEEP_DIRECTIVES = {
    "headline",
    "summary",
    "body",
    "var",
    "instantiate",
    "method",
    "changelog",
    "link",
    "links",
}

DROP_DIRECTIVES = {
    "order-groups",
    "use-constants",
    "use-constructor",
    "internal",
    "advanced",
    "common",
    "hooker",
    "hookable",
    "redirect",
}

PROFILE_CORE = "core"
PROFILE_FULL = "full"

CORE_MODULE_DIRS = []


@dataclass
class ClassInfo:
    name: str
    docblock: str | None
    start: int
    end: int
    rel_path: str
    use_constants: bool
    decl_pos: int


@dataclass
class MemberDoc:
    name: str
    kind: str  # "method" | "const"
    docblock: str
    pos: int
    decl_pos: int


@dataclass
class FileInfo:
    name: str
    rel_path: str
    docblock: str | None
    members: list[MemberDoc]


def strip_docblock(doc: str) -> list[str]:
    lines = doc.splitlines()
    cleaned = []
    for line in lines:
        line = line.lstrip()
        if line.startswith("*"):
            line = line[1:]
            if line.startswith(" "):
                line = line[1:]
        cleaned.append(line.rstrip("\n"))
    return cleaned


def remove_inline_directives(line: str) -> str:
    return re.sub(r"\s*#pw-[A-Za-z0-9_-]+", "", line).rstrip()


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_-]+", "-", value.strip())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug.lower() if slug else "item"


def insert_tag_breaks(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        is_tag = line.lstrip().startswith("@")
        if is_tag and out and out[-1] != "":
            out.append("")
        out.append(line)
    return out


def clean_docblock(lines: list[str], drop_if_internal: bool) -> list[str] | None:
    cleaned: list[str] = []
    in_body_block = False
    internal_flag = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("#pw-body"):
            payload = stripped[len("#pw-body") :].lstrip()
            if payload == "=":
                in_body_block = True
                continue
            if payload == "":
                if in_body_block:
                    in_body_block = False
                continue
            if "#pw-internal" in line:
                internal_flag = True
                continue
            cleaned_payload = remove_inline_directives(payload)
            if cleaned_payload != "":
                cleaned.append(cleaned_payload)
            continue

        if in_body_block:
            if "#pw-internal" in line:
                internal_flag = True
                continue
            cleaned.append(line.rstrip())
            continue

        if "#pw-internal" in line or "@internal" in line:
            internal_flag = True
            continue

        if stripped.startswith("#pw-"):
            match = re.match(r"#pw-([A-Za-z0-9_-]+)(?:\s+(.*))?$", stripped)
            if not match:
                continue
            directive = match.group(1)
            payload = (match.group(2) or "").rstrip()

            if directive in DROP_DIRECTIVES or directive.startswith("group-"):
                continue

            if directive in KEEP_DIRECTIVES or directive.startswith("summary-"):
                if payload:
                    cleaned_payload = remove_inline_directives(payload)
                    if cleaned_payload != "":
                        cleaned.append(cleaned_payload)
                continue

            # Unknown directive: treat as metadata, skip
            continue

        if "@internal" in line:
            internal_flag = True
            continue
        cleaned_line = remove_inline_directives(line)
        if cleaned_line == "" and stripped == "":
            cleaned.append("")
        elif cleaned_line != "":
            cleaned.append(cleaned_line)

    if drop_if_internal and internal_flag:
        return None

    # Trim leading/trailing blank lines
    while cleaned and cleaned[0] == "":
        cleaned.pop(0)
    while cleaned and cleaned[-1] == "":
        cleaned.pop()

    return insert_tag_breaks(cleaned)


def parse_order_groups(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("#pw-order-groups"):
        return []
    payload = stripped[len("#pw-order-groups") :].strip()
    if not payload:
        return []
    return [part.strip() for part in payload.split(",") if part.strip()]


def parse_class_docblock(docblock: str):
    lines = strip_docblock(docblock)
    intro: list[str] = []
    groups: dict[str, list[str]] = {}
    order_groups: list[str] = []
    group_summaries: dict[str, str] = {}
    in_body_block = False
    in_manual_section = False

    def is_underline(text: str) -> bool:
        stripped_line = text.strip()
        return stripped_line != "" and all(ch in "-=" for ch in stripped_line)

    def next_nonempty_line(start_index: int) -> str | None:
        idx = start_index + 1
        while idx < len(lines):
            if lines[idx].strip() != "":
                return lines[idx]
            idx += 1
        return None

    for i, line in enumerate(lines):
        stripped = line.strip()

        if stripped.startswith("#pw-order-groups"):
            order_groups.extend(parse_order_groups(line))
            continue

        if stripped.startswith("#pw-body"):
            payload = stripped[len("#pw-body") :].lstrip()
            if payload == "=":
                in_body_block = True
                continue
            if payload == "":
                if in_body_block:
                    in_body_block = False
                continue
            if "#pw-internal" in line:
                continue
            cleaned_payload = remove_inline_directives(payload)
            if cleaned_payload != "":
                intro.append(cleaned_payload)
            continue

        if in_body_block:
            if "#pw-internal" in line:
                continue
            intro.append(remove_inline_directives(line))
            continue

        if "#pw-internal" in line or "@internal" in line:
            continue

        if stripped.startswith("#pw-"):
            match = re.match(r"#pw-([A-Za-z0-9_-]+)(?:\s+(.*))?$", stripped)
            if not match:
                continue
            directive = match.group(1)
            payload = (match.group(2) or "").rstrip()

            if directive in DROP_DIRECTIVES or directive.startswith("group-"):
                continue

            if directive.startswith("summary-"):
                group_name = directive[len("summary-") :].strip()
                if group_name and payload:
                    group_summaries[group_name] = remove_inline_directives(payload)
                continue

            if directive in KEEP_DIRECTIVES or directive.startswith("summary-"):
                if payload:
                    cleaned_payload = remove_inline_directives(payload)
                    if cleaned_payload != "":
                        intro.append(cleaned_payload)
                continue

            continue

        if stripped.endswith(":") or is_underline(stripped):
            intro.append(remove_inline_directives(line))
            in_manual_section = True
            continue

        if stripped.startswith("@property") or stripped.startswith("@method"):
            groups_found = re.findall(r"#pw-group-([A-Za-z0-9_-]+)", line)
            cleaned_line = remove_inline_directives(line)
            if in_manual_section:
                intro.append(cleaned_line)
            else:
                if not groups_found:
                    groups_found = ["other"]
                for group in groups_found:
                    groups.setdefault(group, []).append(cleaned_line)
            continue

        if stripped.startswith("@"):
            cleaned_line = remove_inline_directives(line)
            intro.append(cleaned_line)
            continue

        cleaned_line = remove_inline_directives(line)
        if cleaned_line == "" and stripped == "":
            intro.append("")
            if in_manual_section:
                next_line = next_nonempty_line(i)
                if next_line is None:
                    in_manual_section = False
                else:
                    if not next_line.strip().startswith("@") and not is_underline(next_line):
                        in_manual_section = False
        elif cleaned_line != "":
            intro.append(cleaned_line)

    while intro and intro[0] == "":
        intro.pop(0)
    while intro and intro[-1] == "":
        intro.pop()

    intro = insert_tag_breaks(intro)

    for group_name, group_lines in list(groups.items()):
        while group_lines and group_lines[0] == "":
            group_lines.pop(0)
        while group_lines and group_lines[-1] == "":
            group_lines.pop()
        groups[group_name] = insert_tag_breaks(group_lines)

    return intro, groups, order_groups, group_summaries


def mask_strings_and_comments(text: str) -> str:
    chars = list(text)
    i = 0
    n = len(chars)
    in_single = False
    in_double = False
    in_line_comment = False
    in_block_comment = False

    while i < n:
        ch = chars[i]
        nxt = chars[i + 1] if i + 1 < n else ""

        if in_line_comment:
            if ch == "\n":
                in_line_comment = False
            else:
                chars[i] = " "
            i += 1
            continue

        if in_block_comment:
            if ch == "*" and nxt == "/":
                chars[i] = " "
                chars[i + 1] = " "
                in_block_comment = False
                i += 2
            else:
                chars[i] = " "
                i += 1
            continue

        if in_single:
            chars[i] = " "
            if ch == "\\" and nxt:
                chars[i + 1] = " "
                i += 2
                continue
            if ch == "'":
                in_single = False
            i += 1
            continue

        if in_double:
            chars[i] = " "
            if ch == "\\" and nxt:
                chars[i + 1] = " "
                i += 2
                continue
            if ch == '"':
                in_double = False
            i += 1
            continue

        if ch == "/" and nxt == "/":
            chars[i] = " "
            chars[i + 1] = " "
            in_line_comment = True
            i += 2
            continue
        if ch == "#" and not in_single and not in_double:
            chars[i] = " "
            in_line_comment = True
            i += 1
            continue
        if ch == "/" and nxt == "*":
            chars[i] = " "
            chars[i + 1] = " "
            in_block_comment = True
            i += 2
            continue
        if ch == "'":
            chars[i] = " "
            in_single = True
            i += 1
            continue
        if ch == '"':
            chars[i] = " "
            in_double = True
            i += 1
            continue

        i += 1

    return "".join(chars)


def find_class_docblock(text: str, class_pos: int) -> str | None:
    docblocks = list(DOCBLOCK_RE.finditer(text, 0, class_pos))
    if not docblocks:
        return None
    for match in reversed(docblocks):
        between = text[match.end() : class_pos]
        if re.match(r"^\s*$", between):
            return match.group(1)
    return None


def iter_php_files(source_dir: Path, profile: str) -> Iterable[Path]:
    rels: list[str]
    if profile == PROFILE_CORE:
        rels = ["wire/core"]
    else:
        rels = ["wire/core", "wire/modules"]

    for rel in rels:
        base = source_dir / rel
        if not base.exists():
            continue
        for path in base.rglob("*.php"):
            if should_skip_path(path):
                continue
            yield path


def find_class_ranges(text: str, rel_path: str) -> list[ClassInfo]:
    masked = mask_strings_and_comments(text)
    classes: list[ClassInfo] = []
    for match in CLASS_DEF_RE.finditer(masked):
        class_name = match.group(2)
        if class_name.startswith("HTMLPurifier") or should_skip_rel(rel_path):
            continue
        class_pos = match.start()
        brace_start = masked.find("{", match.end())
        if brace_start == -1:
            continue
        depth = 1
        i = brace_start + 1
        while i < len(masked) and depth > 0:
            ch = masked[i]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            i += 1
        brace_end = i

        docblock = find_class_docblock(text, class_pos)
        if docblock is not None:
            doc_lines = strip_docblock(docblock)
            if any(line.strip().startswith("#pw-internal") for line in doc_lines):
                continue
        use_constants = docblock is not None and "#pw-use-constants" in docblock
        classes.append(
            ClassInfo(
                name=class_name,
                docblock=docblock,
                start=brace_start,
                end=brace_end,
                rel_path=rel_path,
                use_constants=use_constants,
                decl_pos=class_pos,
            )
        )
    return classes


def should_skip_path(path: Path) -> bool:
    parts_lower = [p.lower() for p in path.parts]
    if any("htmlpurifier" in part for part in parts_lower):
        return True
    if path.name.startswith("HTMLPurifier"):
        return True
    return False


def should_skip_rel(rel_path: str) -> bool:
    parts_lower = [p.lower() for p in Path(rel_path).parts]
    return any("htmlpurifier" in part for part in parts_lower)


def find_first_decl_pos(text: str) -> int | None:
    masked = mask_strings_and_comments(text)
    positions: list[int] = []
    positions.extend(m.start() for m in CLASS_DEF_RE.finditer(masked))
    positions.extend(m.start() for m in FUNC_DECL_AT_RE.finditer(masked))
    positions.extend(m.start() for m in CONST_DECL_AT_RE.finditer(masked))
    return min(positions) if positions else None


def skip_whitespace(text: str, pos: int) -> int:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    return pos


def skip_line_comment(text: str, pos: int) -> int:
    if text.startswith("//", pos):
        end = text.find("\n", pos)
        return len(text) if end == -1 else end
    if text.startswith("#", pos):
        end = text.find("\n", pos)
        return len(text) if end == -1 else end
    return pos


def skip_block_comment(text: str, pos: int) -> int:
    if text.startswith("/*", pos):
        end = text.find("*/", pos + 2)
        return len(text) if end == -1 else end + 2
    return pos


def skip_attributes(text: str, pos: int) -> int:
    while text.startswith("#[", pos):
        pos += 2
        depth = 1
        while pos < len(text) and depth > 0:
            ch = text[pos]
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
            pos += 1
        pos = skip_whitespace(text, pos)
    return pos


def skip_ws_comments_attrs(text: str, pos: int) -> int:
    while pos < len(text):
        new_pos = skip_whitespace(text, pos)
        if new_pos != pos:
            pos = new_pos
            continue
        new_pos = skip_line_comment(text, pos)
        if new_pos != pos:
            pos = new_pos
            continue
        new_pos = skip_block_comment(text, pos)
        if new_pos != pos:
            pos = new_pos
            continue
        new_pos = skip_attributes(text, pos)
        if new_pos != pos:
            pos = new_pos
            continue
        break
    return pos


def classify_after_docblock(text: str, pos: int):
    pos = skip_ws_comments_attrs(text, pos)
    if pos >= len(text):
        return None
    m = CLASS_DECL_AT_RE.match(text, pos)
    if m:
        return ("class", m.group(2), pos)
    m = FUNC_DECL_AT_RE.match(text, pos)
    if m:
        return ("function", m.group(1), pos)
    m = CONST_DECL_AT_RE.match(text, pos)
    if m:
        return ("const", m.group(1), pos)
    return None


def parse_docblocks(text: str, has_classes: bool):
    class_docblocks: dict[int, str] = {}
    members: list[MemberDoc] = []
    file_docblock: str | None = None

    def has_function_tags(doc_text: str) -> bool:
        return re.search(r"^\s*@(?:param|return|throws|see|since|deprecated|var|method|property)\b", doc_text, re.M) is not None

    first_decl_pos = find_first_decl_pos(text)

    for match in DOCBLOCK_RE.finditer(text):
        doc = match.group(1)
        if (
            not has_classes
            and file_docblock is None
            and first_decl_pos is not None
            and match.start() < first_decl_pos
            and not has_function_tags(doc)
        ):
            file_docblock = doc
            continue

        decl = classify_after_docblock(text, match.end())
        if not decl:
            continue
        kind, name, decl_pos = decl
        if kind == "class":
            class_docblocks[decl_pos] = doc
        elif kind == "function":
            members.append(MemberDoc(name=name, kind="method", docblock=doc, pos=match.start(), decl_pos=decl_pos))
        elif kind == "const":
            members.append(MemberDoc(name=name, kind="const", docblock=doc, pos=match.start(), decl_pos=decl_pos))

    return class_docblocks, members, file_docblock


def write_doc(
    out_dir: Path,
    rel_path: str,
    class_info: ClassInfo,
    members: list[MemberDoc],
):
    class_dir = out_dir / Path(rel_path).parent / class_info.name
    class_dir.mkdir(parents=True, exist_ok=True)
    index_path = class_dir / "index.md"

    lines: list[str] = []
    lines.append(f"# {class_info.name}")
    lines.append("")
    lines.append(f"Source: `{rel_path}`")
    lines.append("")

    ordered_names: list[str] = []
    grouped: dict[str, list[str]] = {}
    group_summaries: dict[str, str] = {}

    if class_info.docblock:
        intro_lines, grouped, order_groups, group_summaries = parse_class_docblock(class_info.docblock)
        if intro_lines:
            lines.extend(intro_lines)
        if grouped:
            remaining = sorted(grouped.keys(), key=lambda k: k.lower())
            for name in order_groups:
                lower = name.lower()
                matches = [g for g in grouped.keys() if g.lower() == lower]
                for g in matches:
                    if g not in ordered_names:
                        ordered_names.append(g)
                        if g in remaining:
                            remaining.remove(g)
            for g in remaining:
                if g not in ordered_names:
                    ordered_names.append(g)

            lines.append("")
            lines.append("Groups:")
            for group_name in ordered_names:
                group_file = f"group-{slugify(group_name)}.md"
                lines.append(f"Group: [{group_name}]({group_file})")

    members_sorted = sorted(members, key=lambda m: m.pos)
    method_links: list[str] = []
    const_links: list[str] = []
    for member in members_sorted:
        cleaned = clean_docblock(strip_docblock(member.docblock), drop_if_internal=True)
        if not cleaned:
            continue
        if member.kind == "method":
            method_links.append(f"Method: [{member.name}()](method-{slugify(member.name)}.md)")
        else:
            const_links.append(f"Const: [{member.name}](const-{slugify(member.name)}.md)")

    if method_links:
        lines.append("")
        lines.append("Methods:")
        lines.extend(method_links)
    if const_links:
        lines.append("")
        lines.append("Constants:")
        lines.extend(const_links)

    index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    # Write group files
    if class_info.docblock:
        intro_lines, grouped, order_groups, group_summaries = parse_class_docblock(class_info.docblock)
        ordered_names: list[str] = []
        remaining = sorted(grouped.keys(), key=lambda k: k.lower())
        for name in order_groups:
            lower = name.lower()
            matches = [g for g in grouped.keys() if g.lower() == lower]
            for g in matches:
                if g not in ordered_names:
                    ordered_names.append(g)
                    if g in remaining:
                        remaining.remove(g)
        for g in remaining:
            if g not in ordered_names:
                ordered_names.append(g)

        summary_map = {k.lower(): v for k, v in group_summaries.items()}
        for group_name in ordered_names:
            group_lines = grouped.get(group_name, [])
            if not group_lines:
                continue
            group_path = class_dir / f"group-{slugify(group_name)}.md"
            group_content: list[str] = [
                f"# {class_info.name}: {group_name}",
                "",
                f"Source: `{rel_path}`",
                "",
            ]
            summary = summary_map.get(group_name.lower())
            if summary:
                group_content.append(summary)
                group_content.append("")
            group_content.extend(group_lines)
            group_path.write_text("\n".join(group_content).rstrip() + "\n", encoding="utf-8")

    # Write member files
    for member in members_sorted:
        cleaned = clean_docblock(strip_docblock(member.docblock), drop_if_internal=True)
        if not cleaned:
            continue
        if member.kind == "method":
            member_path = class_dir / f"method-{slugify(member.name)}.md"
            title = f"# {class_info.name}::{member.name}()"
        else:
            member_path = class_dir / f"const-{slugify(member.name)}.md"
            title = f"# {class_info.name}::{member.name}"
        member_content = [
            title,
            "",
            f"Source: `{rel_path}`",
            "",
        ]
        member_content.extend(cleaned)
        member_path.write_text("\n".join(member_content).rstrip() + "\n", encoding="utf-8")

    meta = {
        "type": "class",
        "name": class_info.name,
        "source": rel_path,
        "index": (class_dir / "index.md").as_posix(),
        "groups": [],
        "methods": [],
        "constants": [],
    }
    if class_info.docblock:
        for group_name in ordered_names:
            group_lines = grouped.get(group_name, [])
            if not group_lines:
                continue
            meta["groups"].append(
                {
                    "name": group_name,
                    "file": (class_dir / f"group-{slugify(group_name)}.md").as_posix(),
                }
            )
    for member in members_sorted:
        cleaned = clean_docblock(strip_docblock(member.docblock), drop_if_internal=True)
        if not cleaned:
            continue
        entry = {
            "name": member.name,
            "file": (
                class_dir
                / (
                    f"method-{slugify(member.name)}.md"
                    if member.kind == "method"
                    else f"const-{slugify(member.name)}.md"
                )
            ).as_posix(),
        }
        if member.kind == "method":
            meta["methods"].append(entry)
        else:
            meta["constants"].append(entry)

    return meta


def write_file_doc(out_dir: Path, file_info: FileInfo):
    file_dir = out_dir / Path(file_info.rel_path).parent / file_info.name
    file_dir.mkdir(parents=True, exist_ok=True)
    index_path = file_dir / "index.md"

    lines: list[str] = []
    lines.append(f"# {file_info.name}")
    lines.append("")
    lines.append(f"Source: `{file_info.rel_path}`")
    lines.append("")

    if file_info.docblock:
        file_lines = clean_docblock(strip_docblock(file_info.docblock), drop_if_internal=True)
        if file_lines:
            lines.extend(file_lines)

    members_sorted = sorted(file_info.members, key=lambda m: m.pos)
    method_links: list[str] = []
    const_links: list[str] = []
    for member in members_sorted:
        cleaned = clean_docblock(strip_docblock(member.docblock), drop_if_internal=True)
        if not cleaned:
            continue
        if member.kind == "method":
            method_links.append(f"Method: [{member.name}()](method-{slugify(member.name)}.md)")
        else:
            const_links.append(f"Const: [{member.name}](const-{slugify(member.name)}.md)")

    if method_links:
        lines.append("")
        lines.append("Methods:")
        lines.extend(method_links)
    if const_links:
        lines.append("")
        lines.append("Constants:")
        lines.extend(const_links)

    index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    for member in members_sorted:
        cleaned = clean_docblock(strip_docblock(member.docblock), drop_if_internal=True)
        if not cleaned:
            continue
        if member.kind == "method":
            member_path = file_dir / f"method-{slugify(member.name)}.md"
            title = f"# {file_info.name}::{member.name}()"
        else:
            member_path = file_dir / f"const-{slugify(member.name)}.md"
            title = f"# {file_info.name}::{member.name}"
        member_content = [
            title,
            "",
            f"Source: `{file_info.rel_path}`",
            "",
        ]
        member_content.extend(cleaned)
        member_path.write_text("\n".join(member_content).rstrip() + "\n", encoding="utf-8")

    meta = {
        "type": "file",
        "name": file_info.name,
        "source": file_info.rel_path,
        "index": (file_dir / "index.md").as_posix(),
        "methods": [],
        "constants": [],
    }
    for member in members_sorted:
        cleaned = clean_docblock(strip_docblock(member.docblock), drop_if_internal=True)
        if not cleaned:
            continue
        entry = {
            "name": member.name,
            "file": (
                file_dir
                / (
                    f"method-{slugify(member.name)}.md"
                    if member.kind == "method"
                    else f"const-{slugify(member.name)}.md"
                )
            ).as_posix(),
        }
        if member.kind == "method":
            meta["methods"].append(entry)
        else:
            meta["constants"].append(entry)

    return meta


def build_index(out_dir: Path, items: list[tuple[str, str]]):
    index_path = out_dir / "index.md"
    lines = ["# ProcessWire API (Extracted)", "", "## Docs", ""]
    for rel_path, class_name in sorted(items, key=lambda x: x[1].lower()):
        doc_path = (Path(rel_path).parent / class_name / "index.md").as_posix()
        lines.append(f"- [{class_name}]({doc_path})")
    index_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def prune_skipped_docs(out_dir: Path):
    for path in list(out_dir.rglob("*.md")):
        if should_skip_path(path):
            path.unlink()
    # Remove empty directories
    for path in sorted(out_dir.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass


def clean_output_dir(out_dir: Path):
    for path in list(out_dir.rglob("*.md")):
        path.unlink()
    for path in sorted(out_dir.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Path to ProcessWire source root")
    parser.add_argument("--out", required=True, help="Output directory for docs")
    parser.add_argument("--profile", choices=[PROFILE_CORE, PROFILE_FULL], default=PROFILE_FULL)
    args = parser.parse_args()

    source_dir = Path(args.source)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    clean_output_dir(out_dir)
    prune_skipped_docs(out_dir)

    written: list[tuple[str, str]] = []
    manifest: dict = {
        "profile": args.profile,
        "items": [],
    }
    for src_path in iter_php_files(source_dir, args.profile):
        rel_path = src_path.relative_to(source_dir).as_posix()
        text = src_path.read_text(encoding="utf-8", errors="replace")
        classes = find_class_ranges(text, rel_path)
        class_docblocks, member_docs, file_docblock = parse_docblocks(text, has_classes=bool(classes))

        for class_info in classes:
            if class_info.decl_pos in class_docblocks:
                class_info.docblock = class_docblocks[class_info.decl_pos]
            members: list[MemberDoc] = []
            for doc in member_docs:
                if class_info.start <= doc.decl_pos <= class_info.end:
                    members.append(doc)
            if class_info.use_constants:
                # constants are already in member_docs
                pass

            meta = write_doc(out_dir, rel_path, class_info, members)
            written.append((rel_path, class_info.name))
            manifest["items"].append(meta)

        if not classes:
            file_members = [m for m in member_docs if not any(c.start <= m.decl_pos <= c.end for c in classes)]
            file_name = Path(rel_path).stem
            file_info = FileInfo(name=file_name, rel_path=rel_path, docblock=file_docblock, members=file_members)
            if file_info.docblock or file_info.members:
                meta = write_file_doc(out_dir, file_info)
                written.append((rel_path, file_info.name))
                manifest["items"].append(meta)

    if written:
        build_index(out_dir, written)
        manifest_path = out_dir / "_manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
