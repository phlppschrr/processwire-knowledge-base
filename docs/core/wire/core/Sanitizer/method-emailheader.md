# $sanitizer->emailHeader($value, $headerName = false): string

Source: `wire/core/Sanitizer.php`

Returns a value that may be used in an email header

This method is designed to prevent one email header from injecting into another.

## Usage

~~~~~
// basic usage
$string = $sanitizer->emailHeader($value);

// usage with all arguments
$string = $sanitizer->emailHeader($value, $headerName = false);
~~~~~

## Arguments

- `$value` `string`
- `$headerName` (optional) `bool` Sanitize a header name rather than header value? (default=false) Since 3.0.132

## Return value

- `string`
