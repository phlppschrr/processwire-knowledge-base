# $pagesEditor->move(Page $child, $parent, array $options = array()): bool

Source: `wire/core/PagesEditor.php`

Move page to specified parent (work in progress)

This method is the same as changing a page parent and saving, but provides a useful shortcut
for some cases with less code. This method:

- Does not save the other custom fields of a page (if any are changed).
- Does not require that output formatting be off (it manages that internally).

## Arguments

- `$child` `Page` Page that you want to move.
- `$parent` `Page|int|string` Parent to move it under (may be Page object, path string, or ID integer).
- `$options` (optional) `array` Options to modify behavior (see PagesEditor::save for options).

## Return value

bool True on success or false if not necessary.

## Throws

- WireException if given parent does not exist, or move is not allowed
