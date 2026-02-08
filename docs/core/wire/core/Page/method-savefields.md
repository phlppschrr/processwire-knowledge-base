# $page->saveFields($fields, array $options = array()): array

Source: `wire/core/Page.php`

Save only the given named fields for this page

## Arguments

- `$fields` `array|string` Array of field name(s) or string (CSV or space separated)
- `$options` (optional) `array` See Pages::save() documentation for options.

## Return value

array Names of fields that were saved

## Throws

- WireException on database error

## See also

- [Page::save()](method-save.md)

## Since

3.0.242
