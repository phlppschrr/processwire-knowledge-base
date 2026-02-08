# $sanitizer->maxLength($value, $maxLength = 128, $maxBytes = null): array|float|int|string

Source: `wire/core/Sanitizer.php`

Limit length of given value to that specified

- For strings, this limits the length to that many characters.
- For arrays, the maxLength is assumed to be the max allowed array items.
- For integers maxLength is assumed to be the max allowed digits.
- For floats, maxLength is assumed to be max allowed digits (including decimal point).
- Returns the same type it is given: string, array, int or float

## Arguments

- `$value` `string|int|array|float`
- `$maxLength` (optional) `int` Maximum length (default=128)
- `$maxBytes` (optional) `null|int` Maximum allowed bytes (used for string types only)

## Return value

array|float|int|string

## See also

- [Sanitizer::minLength()](method-minlength.md)

## Since

3.0.125
