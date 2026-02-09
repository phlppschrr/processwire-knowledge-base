# $wireArray->set($key, $value): $this

Source: `wire/core/WireArray.php`

Set an item by key in the WireArray.

## Usage

~~~~~
// basic usage
$result = $wireArray->set($key, $value);
~~~~~

## Arguments

- `$key` `int|string` Key of item to set.
- `$value` `int|string|array|object|Wire` Item value to set.

## Return value

- `$this`

## Exceptions

- `WireException` If given an item not compatible with this WireArray.
