# $sanitizer->textarea($value, $options = array()): string

Source: `wire/core/Sanitizer.php`

Sanitize input string as multi-line text without HTML tags

- This sanitizer is useful for user-submitted text from a plain-text `<textarea>` field,
  or any other kind of string value that might have multiple-lines.

- Don’t use this sanitizer for values where you want to allow HTML (like rich text fields).
  For those values you should instead use the `$sanitizer->purify()` method.

- If using returned value for front-end output, be sure to run it through `$sanitizer->entities()` first.

## Arguments

- string $value String value to sanitize
- array $options Options to modify default behavior - `maxLength` (int): maximum characters allowed, or 0=no max (default=16384 or 16kb). - `maxBytes` (int): maximum bytes allowed (default=0, which implies maxLength*4 or 64kb). - `stripTags` (bool): strip markup tags? (default=true). - `stripMB4` (bool): strip emoji and other 4-byte UTF-8? (default=false). - `stripIndents` (bool): Remove indents (space/tabs) at the beginning of lines? (default=false). Since 3.0.105 - `reduceSpace` (bool|string): reduce consecutive whitespace to single? Specify true or character to reduce to (default=false). Since 3.0.105 - `allowableTags` (string): markup tags that are allowed, if stripTags is true (use same format as for PHP's `strip_tags()` function. - `convertEntities` (bool): convert HTML entities to equivalent character(s)? (default=false). Since 3.0.105 - `truncateTail` (bool): if truncate necessary for maxLength, truncate from end/tail? Use false to truncate head (default=true). Since 3.0.105 - `allowCRLF` (bool): allow CR+LF newlines (i.e. "\r\n")? (default=false, which means "\r\n" is replaced with "\n"). - `inCharset` (string): input character set (default="UTF-8"). - `outCharset` (string): output character set (default="UTF-8").

## Return value

string

## See also

- [Sanitizer::text()](method-text.md)
- [Sanitizer::purify()](method-purify.md)
