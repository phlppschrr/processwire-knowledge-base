# $sanitizer->match($value, $regex): string

Source: `wire/core/Sanitizer.php`

Validate that given value matches regex pattern.

If given value matches, value is returned. If not, blank is returned.

## Arguments

- string $value Value to match
- string $regex PCRE regex pattern (same as you would provide to PHP's `preg_match()`)

## Return value

string Value you supplied if it matches, or blank string if it doesn't
