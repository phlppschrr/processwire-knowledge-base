# $sanitizer->int($value, array $options = array()): int

Source: `wire/core/Sanitizer.php`

Sanitized an integer (unsigned, unless you specify a negative minimum value)

## Arguments

- mixed $value Value you want to sanitize as an integer
- array $options Optionally specify any one or more of the following to modify behavior: - `min` (int|null): Minimum allowed value (default=0) - `max` (int|null): Maximum allowed value (default=PHP_INT_MAX) - `blankValue` (mixed): Value that you want to use when provided value is null or blank string (default=0)

## Return value

int Returns integer, or specified blankValue (which doesn't necessarily have to be an integer)
