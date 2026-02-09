# $functions->wireLength($value, $mb = true): int

Source: `wire/core/Functions.php`

Returns string length of any type (string, array, object, bool, int, etc.)

- If given a string it returns the multibyte string length.
- If given a bool, returns 1 for true or 0 for false.
- If given an int or float, returns its length when typecast to string.
- If given array or object it duplicates the behavior of `wireCount()`.
- If given null returns 0.

## Usage

~~~~~
// basic usage
$int = $functions->wireLength($value);

// usage with all arguments
$int = $functions->wireLength($value, $mb = true);
~~~~~

## Arguments

- `$value` `string|array|object|int|bool|null`
- `$mb` (optional) `bool` Use multibyte string length when available (default=true)

## Return value

- `int`

## Since

3.0.192
