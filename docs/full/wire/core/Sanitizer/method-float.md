# Sanitizer::float()

Source: `wire/core/Sanitizer.php`

Sanitize to floating point value

Values for `getString` argument:

- `false` (bool): do not return string value (default). 3.0.171+
- `true` (bool): locale aware floating point number string. 3.0.171+
- `f` (string): locale aware floating point number string (same as true). 3.0.193+
- `F` (string): non-locale aware floating point number string. 3.0.193+
- `e` (string): lowercase scientific notation (e.g. 1.2e+2). 3.0.193+
- `E` (string): uppercase scientific notation (e.g. 1.2E+2). 3.0.193+


@param float|string|int $value

@param array $options Optionally specify one or more options in an associative array:
	- `precision` (int|null): Optional number of digits to round to (default=null)
	- `mode` (int): Mode to use for rounding precision (default=PHP_ROUND_HALF_UP);
	- `blankValue` (null|int|string|float): Value to return (whether float or non-float) if provided $value is an empty non-float (default=0.0)
	- `min` (float|null): Minimum allowed value, excluding blankValue (default=null)
	- `max` (float|null): Maximum allowed value, excluding blankValue (default=null)
 - `getString (bool|string): Return a string rather than float value? 3.0.171+ (default=false). See value options in method description.

@return float|string
