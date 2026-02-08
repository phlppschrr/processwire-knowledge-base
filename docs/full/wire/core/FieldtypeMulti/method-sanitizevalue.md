# $fieldtypeMulti->sanitizeValue(Page $page, Field $field, $value): WireArray

Source: `wire/core/FieldtypeMulti.php`

Per the Fieldtype interface, sanitize the combined value for use in a Page

In this case, make sure that it's a WireArray (able to hold multiple values)

## Usage

~~~~~
// basic usage
$items = $fieldtypeMulti->sanitizeValue($page, $field, $value);

// usage with all arguments
$items = $fieldtypeMulti->sanitizeValue(Page $page, Field $field, $value);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `mixed`

## Return value

- `WireArray`
