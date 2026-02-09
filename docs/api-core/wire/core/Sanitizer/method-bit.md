# $sanitizer->bit($value): int

Source: `wire/core/Sanitizer.php`

Sanitize to a bit, returning only integer 0 or 1

This works the same as the bool sanitizer except that it returns 0 or 1 rather than false or true.

## Usage

~~~~~
// basic usage
$int = $sanitizer->bit($value);
~~~~~

## Arguments

- `$value` `string|int|array`

## Return value

- `int`

## See Also

- [Sanitizer::bool()](method-bool.md)

## Since

3.0.125
