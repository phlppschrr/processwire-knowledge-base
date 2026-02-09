# $fieldgroup->set($key, $value): Fieldgroup|WireArray

Source: `wire/core/Fieldgroup.php`

Set a fieldgroup property

## Usage

~~~~~
// basic usage
$fieldgroup = $fieldgroup->set($key, $value);
~~~~~

## Arguments

- `$key` `string` Name of property to set
- `$value` `string|int|object` Value of property

## Return value

- `Fieldgroup|WireArray` $this

## Exceptions

- `WireException` if passed invalid data
