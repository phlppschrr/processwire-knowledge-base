# Sanitizer::max()

Source: `wire/core/Sanitizer.php`

Sanitize to have a maximuim value

If float or decimal string specified for $max argument, return value will be a float,
otherwise an integer is returned.

~~~~~
$n = 10;
$sanitizer->max(5); // returns 5
$sanitizer->max(100); // returns 10
$sanitizer->max(100.0); // returns 10.0
~~~~~


@param int|float|string $value

@param int|float|string $max Maximum allowed value

@return int|float

@since 3.0.125

@see Sanitizer::min()
