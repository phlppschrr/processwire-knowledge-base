# $fuel->set($key, $value, $lock = false): $this

Source: `wire/core/Fuel.php`


## Arguments

- `$key` `string` API variable name to set - should be valid PHP variable name.
- `$value` `object|mixed` Value for the API variable.
- `$lock` (optional) `bool` Whether to prevent this API variable from being overwritten in the future.

## Return value

$this

## Throws

- WireException When you try to set a previously locked API variable, a WireException will be thrown.
