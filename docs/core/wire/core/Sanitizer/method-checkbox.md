# $sanitizer->checkbox($value, $yes = true, $no = false): int|bool|string|mixed|null

Source: `wire/core/Sanitizer.php`

Sanitize checkbox value

## Arguments

- `$value` `int|bool|string|mixed|null` Value to check
- `$yes` (optional) `int|bool|string|mixed|null` Value to return if checked (default=true)
- `$no` (optional) `int|bool|string|mixed|null` Value to return if not checked (default=false)

## Return value

int|bool|string|mixed|null Return value, based on $checked or $unchecked argument

## See also

- [Sanitizer::bool()](method-bool.md)
- [Sanitizer::bit()](method-bit.md)

## Since

3.0.128
