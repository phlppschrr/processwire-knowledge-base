# $page->getField($field): Field|null

Source: `wire/core/Page.php`

Get a Field object in context or NULL if not valid for this page

Field in context is only returned when output formatting is on.

## Arguments

- `$field` `string|int|Field`

## Return value

Field|null

## Details

- @todo determine if we can always retrieve in context regardless of output formatting.
