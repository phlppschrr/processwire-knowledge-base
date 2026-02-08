# $sanitizer->string($value, $sanitizer = null): string

Source: `wire/core/Sanitizer.php`

Sanitize value to string

Note that this makes no assumptions about what is a "safe" string, so you should always apply another
sanitizer to it.

## Arguments

- `$value` `string|int|array|object|bool|float` Value to sanitize as string
- string|null Optional sanitizer method (from this class) to apply to the string before returning

## Return value

string
