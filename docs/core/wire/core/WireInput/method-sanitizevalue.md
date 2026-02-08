# $wireInput->sanitizeValue($method, $value, $getArray): array|int|float|string|null

Source: `wire/core/WireInput.php`

Sanitize the given value with the given method(s)

## Arguments

- string $method Sanitizer method name or CSV string of sanitizer method names
- string|array|null $value
- bool $getArray

## Return value

array|int|float|string|null

## Throws

- WireException If given unknown sanitizer method
