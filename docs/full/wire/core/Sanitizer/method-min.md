# Sanitizer::min()

Source: `wire/core/Sanitizer.php`

Sanitize to have a minimum value

If float or decimal string specified for $min argument, return value will be a float,
otherwise an integer is returned.

~~~~~
$n = 10;
$sanitizer->min(100); // returns 100
$sanitizer->min(5); // returns 10
$sanitizer->min(1.0); // returns 10.0
~~~~~


@param int|float|string $value

@param int|float|string $min Minimum allowed value

@return int|float

@since 3.0.125

@see Sanitizer::max()
