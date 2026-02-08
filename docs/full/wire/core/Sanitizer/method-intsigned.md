# $sanitizer->intSigned($value, array $options = array()): int

Source: `wire/core/Sanitizer.php`

Sanitize to signed integer (negative or positive)

## Arguments

- mixed $value
- array $options Optionally specify any one or more of the following to modify behavior: - `min` (int|null): Minimum allowed value (default=negative PHP_INT_MAX) - `max` (int|null): Maximum allowed value (default=PHP_INT_MAX) - `blankValue` (mixed): Value that you want to use when provided value is null or blank string (default=0)

## Return value

int
