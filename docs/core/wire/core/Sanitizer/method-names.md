# Sanitizer::names()

Source: `wire/core/Sanitizer.php`

Sanitize a string or array containing multiple names

- Default behavior is to sanitize to ASCII alphanumeric and hyphen, underscore, and period.
- If given a string, multiple names may be separated by a delimeter (which is a space by default).
- Return value will be of the same type as the given value (i.e. string or array).


@param string|array $value Value(s) to sanitize to name format.

@param string $delimeter Character that delimits values, if $value is a string (default=" ").

@param array $allowedExtras Additional characters that are allowed in the value (default=['-', '_', '.']).

@param string $replacementChar Single character replacement value for invalid characters (default='_').

@param bool $beautify Whether or not to beautify returned values (default=false). See Sanitizer::name() for beautify options.

@return string|array Returns string if given a string for $value, returns array if given an array for $value.
