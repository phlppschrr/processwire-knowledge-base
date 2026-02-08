# $page->saveFields($fields, array $options = array()): array

Source: `wire/core/Page.php`

Save only the given named fields for this page

## Arguments

- array|string $fields Array of field name(s) or string (CSV or space separated)
- array $options See Pages::save() documentation for options.

## Return value

array Names of fields that were saved

## Throws

- WireException on database error

## See also

- [Page::save()](method-save.md)

## Meta

- @since 3.0.242
