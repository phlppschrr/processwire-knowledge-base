# Sanitizer::range()

Source: `wire/core/Sanitizer.php`

Sanitize value to be within the given min and max range

If float or decimal string specified for $min or $max arguments, return value will be a float,
otherwise an integer is returned.

~~~~~
$n = 10;
$sanitizer->range($n, 100, 200); // returns 100
$sanitizer->range($n, 0, 1.0); // returns 1.0
$sanitizer->range($n, 1.1, 100.5); // returns 10.0
~~~~~


@param int|float|string $value

@param int|float|string|null $min Minimum allowed value or null for no minimum (default=null)

@param int|float|string|null $max Maximum allowed value or null for no maximum (default=null)

@return int|float

@since 3.0.125
