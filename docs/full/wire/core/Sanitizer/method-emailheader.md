# Sanitizer::emailHeader()

Source: `wire/core/Sanitizer.php`

Returns a value that may be used in an email header

This method is designed to prevent one email header from injecting into another.


@param string $value

@param bool $headerName Sanitize a header name rather than header value? (default=false) Since 3.0.132

@return string
