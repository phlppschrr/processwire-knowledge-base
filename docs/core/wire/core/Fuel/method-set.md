# $fuel->set($key, $value, $lock = false): $this

Source: `wire/core/Fuel.php`


## Arguments

- string $key API variable name to set - should be valid PHP variable name.
- object|mixed $value Value for the API variable.
- bool $lock Whether to prevent this API variable from being overwritten in the future.

## Return value

$this

## Throws

- WireException When you try to set a previously locked API variable, a WireException will be thrown.
