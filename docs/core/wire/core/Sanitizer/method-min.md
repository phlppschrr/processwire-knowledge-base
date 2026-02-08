# $sanitizer->min($value, $min = PHP_INT_MIN): int|float

Source: `wire/core/Sanitizer.php`

Sanitize to have a minimum value

If float or decimal string specified for $min argument, return value will be a float,
otherwise an integer is returned.

## Example

~~~~~
$n = 10;
$sanitizer->min(100); // returns 100
$sanitizer->min(5); // returns 10
$sanitizer->min(1.0); // returns 10.0
~~~~~

## Usage

~~~~~
// basic usage
$int = $sanitizer->min($value);

// usage with all arguments
$int = $sanitizer->min($value, $min = PHP_INT_MIN);
~~~~~

## Arguments

- `$value` `int|float|string`
- `$min` (optional) `int|float|string` Minimum allowed value

## Return value

- `int|float`

## See Also

- [Sanitizer::max()](method-max.md)

## Since

3.0.125
