# $sanitizer->intUnsigned($value, array $options = array()): int

Source: `wire/core/Sanitizer.php`

Sanitize to unsigned (0 or positive) integer

This is an alias to the int() method with default min/max arguments.

## Arguments

- `$value` `mixed`
- `$options` (optional) `array` Optionally specify any one or more of the following to modify behavior: - `min` (int|null): Minimum allowed value (default=0) - `max` (int|null): Maximum allowed value (default=PHP_INT_MAX) - `blankValue` (mixed): Value that you want to use when provided value is null or blank string (default=0)

## Return value

int Returns integer, or specified blankValue (which doesn't necessarily have to be an integer)
