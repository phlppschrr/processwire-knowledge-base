# $sanitizer->max($value, $max = PHP_INT_MAX): int|float

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

## Arguments

- `$value` `int|float|string`
- `$max` (optional) `int|float|string` Maximum allowed value

## Return value

int|float

## See also

- [Sanitizer::min()](method-min.md)

## Since

3.0.125
