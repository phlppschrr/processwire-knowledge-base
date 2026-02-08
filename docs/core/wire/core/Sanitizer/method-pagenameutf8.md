# $sanitizer->pageNameUTF8($value, $maxLength = 128): string

Source: `wire/core/Sanitizer.php`

Sanitize and allow for UTF-8 characters in page name

- If `$config->pageNameCharset` is not `UTF8` then this function just passes control to the regular page name sanitizer.
- Allowed UTF-8 characters are determined from `$config->pageNameWhitelist`.
- This method does not convert to or from UTF-8, it only sanitizes it against the whitelist.
- If given a value that has only ASCII characters, this will pass control to the regular page name sanitizer.

## Arguments

- string $value Value to sanitize
- int $maxLength Maximum number of characters allowed

## Return value

string Sanitized value
