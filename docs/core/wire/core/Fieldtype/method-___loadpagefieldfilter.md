# $fieldtype->___loadPageFieldFilter(Page $page, Field $field, $selector): mixed|null

Source: `wire/core/Fieldtype.php`

Load the given page field from the database table and return a *filtered* value.

This is the same as `Fieldtype::loadPageField()` but enables a selector to be
provided which can filter the returned value.

As far as core Fieldtypes go, this one is only applicable to FieldtypeMulti derived types.

## Arguments

- `$page` `Page` Page object to save.
- `$field` `Field` Field to retrieve from the page.
- `$selector` `Selectors|string|array`

## Return value

mixed|null
