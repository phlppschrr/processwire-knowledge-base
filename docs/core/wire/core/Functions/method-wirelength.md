# $functions->wireLength($value, $mb = true): int

Source: `wire/core/Functions.php`

Returns string length of any type (string, array, object, bool, int, etc.)

- If given a string it returns the multibyte string length.
- If given a bool, returns 1 for true or 0 for false.
- If given an int or float, returns its length when typecast to string.
- If given array or object it duplicates the behavior of `wireCount()`.
- If given null returns 0.

## Arguments

- string|array|object|int|bool|null $value
- bool $mb Use multibyte string length when available (default=true)

## Return value

int

## Meta

- @since 3.0.192
