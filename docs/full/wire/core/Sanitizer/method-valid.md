# $sanitizer->valid($value, $method = 'text', $strict = false): bool

Source: `wire/core/Sanitizer.php`

Is given value valid? (i.e. unchanged by given sanitizer method)

~~~~~~
if($sanitizer->valid('abc123', 'alphanumeric')) {
 // value is valid
}
~~~~~~

## Arguments

- string|int|array|float $value Value to check if valid
- string $method Method name or CSV method names
- bool $strict When true, sanitized value must be identical in type to the one given

## Return value

bool

## Meta

- @since 3.0.125
