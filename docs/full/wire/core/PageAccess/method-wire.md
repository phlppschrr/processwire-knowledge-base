# $pageAccess->wire($name = '', $value = null, $lock = false): mixed|Fuel

Source: `wire/core/PageAccess.php`

Get or inject a ProcessWire API variable or fuel a new object instance

See Wire::wire() for explanation of all options.

## Arguments

- string|WireFuelable $name Name of API variable to retrieve, set, or omit to retrieve entire Fuel object.
- null|mixed $value Value to set if using this as a setter, otherwise omit.
- bool $lock When using as a setter, specify true if you want to lock the value from future changes (default=false)

## Return value

mixed|Fuel

## Throws

- WireException
