# $field->set($key, $value): Field|WireData

Source: `wire/core/Field.php`

Set a native setting or a dynamic data property for this Field

This can also be used directly via `$field->name = 'company';`

## Usage

~~~~~
// basic usage
$field = $field->set($key, $value);
~~~~~

## Arguments

- `$key` `string` Property name to set
- `$value` `mixed`

## Return value

- `Field|WireData`
