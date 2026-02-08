# $sanitizer->emailHeader($value, $headerName = false): string

Source: `wire/core/Sanitizer.php`

Returns a value that may be used in an email header

This method is designed to prevent one email header from injecting into another.

## Arguments

- string $value
- bool $headerName Sanitize a header name rather than header value? (default=false) Since 3.0.132

## Return value

string
