# $fieldsTableTools->valueExists(Field $field, $value, $col = 'data'): int

Source: `wire/core/FieldsTableTools.php`

Does given value exist anywhere in field table?

## Usage

~~~~~
// basic usage
$int = $fieldsTableTools->valueExists($field, $value);

// usage with all arguments
$int = $fieldsTableTools->valueExists(Field $field, $value, $col = 'data');
~~~~~

## Arguments

- `$field` `Field`
- `$value` `string|int`
- `$col` (optional) `string`

## Return value

- `int` Returns page ID where value exists, if found. Otherwise returns 0.

## Exceptions

- `WireException`
