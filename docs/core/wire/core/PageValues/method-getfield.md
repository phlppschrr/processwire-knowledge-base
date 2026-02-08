# $pageValues->getField(Page $page, $field): Field|null

Source: `wire/core/PageValues.php`

Get a Field object in context or NULL if not valid for this page

Field in context is only returned when output formatting is on.

## Arguments

- `$page` `Page`
- `$field` `string|int|Field`

## Return value

Field|null

## Details

- @todo determine if we can always retrieve in context regardless of output formatting.
