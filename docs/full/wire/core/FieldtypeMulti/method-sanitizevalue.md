# $fieldtypeMulti->sanitizeValue(Page $page, Field $field, $value): WireArray

Source: `wire/core/FieldtypeMulti.php`

Per the Fieldtype interface, sanitize the combined value for use in a Page

In this case, make sure that it's a WireArray (able to hold multiple values)

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `mixed`

## Return value

WireArray
