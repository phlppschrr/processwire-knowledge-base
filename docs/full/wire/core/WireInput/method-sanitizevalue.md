# $wireInput->sanitizeValue($method, $value, $getArray): array|int|float|string|null

Source: `wire/core/WireInput.php`

Sanitize the given value with the given method(s)

## Usage

~~~~~
// basic usage
$array = $wireInput->sanitizeValue($method, $value, $getArray);
~~~~~

## Arguments

- `$method` `string` Sanitizer method name or CSV string of sanitizer method names
- `$value` `string|array|null`
- `$getArray` `bool`

## Return value

- `array|int|float|string|null`

## Exceptions

- `WireException` If given unknown sanitizer method
