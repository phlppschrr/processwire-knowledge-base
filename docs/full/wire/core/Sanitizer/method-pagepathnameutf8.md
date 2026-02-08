# Sanitizer::pagePathNameUTF8()

Source: `wire/core/Sanitizer.php`

Sanitize a UTF-8 page path name (does not perform ASCII/UTF8 conversions)

- If `$config->pageNameCharset` is not `UTF8` then this does the same thing as `$sanitizer->pagePathName()`.
- Returned path is not guaranteed to be valid or match a page, just sanitized.


@param string $value Path name to sanitize

@return string

@see Sanitizer::pagePathName()
