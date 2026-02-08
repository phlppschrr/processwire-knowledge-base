# ProcessWire PHPDoc Custom Syntax (Discovery Notes)

Scope: initial discovery from core classes `Wire`, `Page`, `Pages`, `Field`, `Template`, `Inputfield`, plus a few targeted examples (`Notice`, `Module`, `WireArray`, `Modules`, `Pagefile`).

## 1) Inline directives (`#pw-*`) inside docblocks
These appear either on their own line or appended to standard `@property` / `@method` lines.

### A. Class-level docblock directives
Seen in class docblocks at top of file:

- `#pw-headline <text>`
  - Example: `Notice` uses `#pw-headline Notice`.
- `#pw-summary <text>`
  - Short summary line.
- `#pw-summary-<group> <text>`
  - Group-specific summary. Example: `Page` uses `#pw-summary-languages`, `#pw-summary-system`, `#pw-summary-previous`.
- `#pw-body <text>` or `#pw-body =` … `#pw-body`
  - Single-line body or multi-line body block.
  - Multi-line form uses a start marker `#pw-body =` and a closing marker `#pw-body`.
- `#pw-order-groups <comma-separated list>`
  - Example: `Page` uses `#pw-order-groups common,traversal,manipulation,...`.
- `#pw-use-constants`
  - Indicates constants should be documented.
- `#pw-use-constructor`
  - Seen in `Notice` to include constructor details.
- `#pw-var <variable>`
  - Example: `Field` uses `#pw-var $field`.
- `#pw-instantiate <code>`
  - Example: `Field` uses `#pw-instantiate $field = $fields->get('field_name');`.

### B. Per-item directives on `@property`, `@method`, etc.
These often appear at end of the line, multiple per line.

- `#pw-group-<name>`
  - Assigns groups. Multiple groups may appear on one line.
  - Group names can include uppercase letters and hyphens: e.g. `#pw-group-URLs`, `#pw-group-HTTP-and-input`.
- `#pw-internal`
  - Marks internal items.
- `#pw-advanced`, `#pw-common`, `#pw-hooker`, `#pw-hookable`
  - Used as flags or pseudo-groups.

### C. Method/class metadata directives
Used inside method docblocks:

- `#pw-links <text>` / `#pw-link <text>`
  - Can include Markdown links. Example: `Page::setAndSave()` uses `#pw-links [Blog post about setAndSave](https://processwire.com/...)`.
- `#pw-redirect <ClassName>`
  - Used in `Pages` helper accessors to point to helper class.
- `#pw-changelog <version> <text>`
  - Seen in `Modules` and `Pagefile`.
- `#pw-method <signature>`
  - Seen in `Module` class docblock to list expected module API methods.

## 2) Standard PHPDoc tags with custom suffixes
Examples from `Wire`, `Page`, `Pages`, `Field`, `Template`:

- `@property ... #pw-group-<name> #pw-internal`
- `@method ... #pw-group-<name>`
- `@link <url> <text>` (standard tag, URLs should be preserved verbatim)

These should be parsed while retaining the exact raw text of the line.

## 3) Multi-line body blocks
Pattern (from `Wire` and `Pages`):

```
#pw-body =
<multiple lines>
#pw-body
```

The lines between are the body content. Preserve them as-is (including indentation and list markers).

## 4) Embedded code fences in docblocks
Docblocks sometimes include `~~~~~` fences for code examples (e.g. `Page::setAndSave()`). These are part of the original text and should be preserved verbatim.

## 5) Notes for parser design
- Treat any `#pw-*` token as a directive. Some are flags (no trailing text), others carry a payload (rest of line).
- Multiple directives can exist on one line; parse all without mutating the original line text.
- `#pw-group-<name>` may appear multiple times on a line. Group names are case sensitive and can contain hyphens.
- `#pw-body` can be inline or block-form. Block form uses `#pw-body =` to open and `#pw-body` to close.
- Preserve the raw line text (after stripping leading `*`), because the output must match source wording exactly.

