# $pageAccess->wire($name = '', $value = null, $lock = false): mixed|Fuel

Source: `wire/core/PageAccess.php`

Get or inject a ProcessWire API variable or fuel a new object instance

See Wire::wire() for explanation of all options.

## Usage

~~~~~
// basic usage
$result = $pageAccess->wire();

// usage with all arguments
$result = $pageAccess->wire($name = '', $value = null, $lock = false);
~~~~~

## Arguments

- `$name` (optional) `string|WireFuelable` Name of API variable to retrieve, set, or omit to retrieve entire Fuel object.
- `$value` (optional) `null|mixed` Value to set if using this as a setter, otherwise omit.
- `$lock` (optional) `bool` When using as a setter, specify true if you want to lock the value from future changes (default=false)

## Return value

- `mixed|Fuel`

## Exceptions

- `WireException`
