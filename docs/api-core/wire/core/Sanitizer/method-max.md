# $sanitizer->max($value, $max = PHP_INT_MAX): int|float

Source: `wire/core/Sanitizer.php`

Sanitize to have a maximuim value

If float or decimal string specified for $max argument, return value will be a float,
otherwise an integer is returned.

## Example

~~~~~
$n = 10;
$sanitizer->max(5); // returns 5
$sanitizer->max(100); // returns 10
$sanitizer->max(100.0); // returns 10.0
~~~~~

## Usage

~~~~~
// basic usage
$int = $sanitizer->max($value);

// usage with all arguments
$int = $sanitizer->max($value, $max = PHP_INT_MAX);
~~~~~

## Arguments

- `$value` `int|float|string`
- `$max` (optional) `int|float|string` Maximum allowed value

## Return value

- `int|float`

## See Also

- [Sanitizer::min()](method-min.md)

## Since

3.0.125
