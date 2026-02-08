# $sanitizer->names($value, $delimeter = ' ', $allowedExtras = array('-', '_', '.'), $replacementChar = '_', $beautify = false): string|array

Source: `wire/core/Sanitizer.php`

Sanitize a string or array containing multiple names

- Default behavior is to sanitize to ASCII alphanumeric and hyphen, underscore, and period.
- If given a string, multiple names may be separated by a delimeter (which is a space by default).
- Return value will be of the same type as the given value (i.e. string or array).

## Arguments

- string|array $value Value(s) to sanitize to name format.
- string $delimeter Character that delimits values, if $value is a string (default=" ").
- array $allowedExtras Additional characters that are allowed in the value (default=['-', '_', '.']).
- string $replacementChar Single character replacement value for invalid characters (default='_').
- bool $beautify Whether or not to beautify returned values (default=false). See Sanitizer::name() for beautify options.

## Return value

string|array Returns string if given a string for $value, returns array if given an array for $value.
