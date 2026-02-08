# $sanitizer->valid($value, $method = 'text', $strict = false): bool

Source: `wire/core/Sanitizer.php`

Is given value valid? (i.e. unchanged by given sanitizer method)

~~~~~~
if($sanitizer->valid('abc123', 'alphanumeric')) {
 // value is valid
}
~~~~~~

## Arguments

- `$value` `string|int|array|float` Value to check if valid
- `$method` (optional) `string` Method name or CSV method names
- `$strict` (optional) `bool` When true, sanitized value must be identical in type to the one given

## Return value

bool

## Since

3.0.125
