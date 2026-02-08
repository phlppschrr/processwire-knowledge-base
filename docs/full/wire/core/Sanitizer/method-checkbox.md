# $sanitizer->checkbox($value, $yes = true, $no = false): int|bool|string|mixed|null

Source: `wire/core/Sanitizer.php`

Sanitize checkbox value

## Usage

~~~~~
// basic usage
$int = $sanitizer->checkbox($value);

// usage with all arguments
$int = $sanitizer->checkbox($value, $yes = true, $no = false);
~~~~~

## Arguments

- `$value` `int|bool|string|mixed|null` Value to check
- `$yes` (optional) `int|bool|string|mixed|null` Value to return if checked (default=true)
- `$no` (optional) `int|bool|string|mixed|null` Value to return if not checked (default=false)

## Return value

- `int|bool|string|mixed|null` Return value, based on $checked or $unchecked argument

## See Also

- [Sanitizer::bool()](method-bool.md)
- [Sanitizer::bit()](method-bit.md)

## Since

3.0.128
