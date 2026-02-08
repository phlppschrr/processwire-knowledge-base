# $sanitizer->checkbox($value, $yes = true, $no = false): int|bool|string|mixed|null

Source: `wire/core/Sanitizer.php`

Sanitize checkbox value

## Arguments

- int|bool|string|mixed|null $value Value to check
- int|bool|string|mixed|null $yes Value to return if checked (default=true)
- int|bool|string|mixed|null $no Value to return if not checked (default=false)

## Return value

int|bool|string|mixed|null Return value, based on $checked or $unchecked argument

## See also

- [Sanitizer::bool()](method-bool.md)
- [Sanitizer::bit()](method-bit.md)

## Meta

- @since 3.0.128
