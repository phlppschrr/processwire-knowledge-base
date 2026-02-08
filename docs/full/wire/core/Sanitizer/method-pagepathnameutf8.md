# $sanitizer->pagePathNameUTF8($value): string

Source: `wire/core/Sanitizer.php`

Sanitize a UTF-8 page path name (does not perform ASCII/UTF8 conversions)

- If `$config->pageNameCharset` is not `UTF8` then this does the same thing as `$sanitizer->pagePathName()`.
- Returned path is not guaranteed to be valid or match a page, just sanitized.

## Usage

~~~~~
// basic usage
$string = $sanitizer->pagePathNameUTF8($value);
~~~~~

## Arguments

- `$value` `string` Path name to sanitize

## Return value

- `string`

## See Also

- [Sanitizer::pagePathName()](method-pagepathname.md)
