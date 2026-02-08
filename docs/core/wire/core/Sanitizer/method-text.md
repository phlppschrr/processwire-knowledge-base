# $sanitizer->text($value, $options = array()): string

Source: `wire/core/Sanitizer.php`

Sanitize short string of text to single line without HTML

- This sanitizer is useful for short strings of input text like like first and last names, street names, search queries, etc.

- Please note the default 255 character max length setting.

- If using returned value for front-end output, be sure to run it through `$sanitizer->entities()` first.

~~~~~
$str = "
  <strong>Hello World</strong>
  How are you doing today?
";

echo $sanitizer->text($str);
// outputs: Hello World How are you doing today?
~~~~~

## Arguments

- `$value` `string` String value to sanitize
- `$options` (optional) `array` Options to modify default behavior: - `maxLength` (int): maximum characters allowed, or 0=no max (default=255). - `maxBytes` (int): maximum bytes allowed (default=0, which implies maxLength*4). - `stripTags` (bool): strip markup tags? (default=true). - `stripMB4` (bool): strip emoji and other 4-byte UTF-8? (default=false). - `stripQuotes` (bool): strip out any "quote" or 'quote' characters? Specify true, or character to replace with. (default=false) - `stripSpace` (bool|string): strip whitespace? Specify true or character to replace whitespace with (default=false). Since 3.0.105 - `reduceSpace` (bool|string): reduce consecutive whitespace to single? Specify true or character to reduce to (default=false). Note that the reduceSpace option is an alternative to the stripSpace option, they should not be used together. Since 3.0.105 - `allowableTags` (string): markup tags that are allowed, if stripTags is true (use same format as for PHP's `strip_tags()` function. - `multiLine` (bool): allow multiple lines? if false, then $newlineReplacement below is applicable (default=false). - `convertEntities` (bool): convert HTML entities to equivalent character(s)? (default=false). Since 3.0.105 - `newlineReplacement` (string): character to replace newlines with, OR specify boolean true to remove extra lines (default=" "). - `truncateTail` (bool): if truncate necessary for maxLength, truncate from end/tail? Use false to truncate head (default=true). Since 3.0.105 - `inCharset` (string): input character set (default="UTF-8"). - `outCharset` (string): output character set (default="UTF-8").

## Return value

string

## See also

- [Sanitizer::textarea()](method-textarea.md)
- [Sanitizer::line()](method-line.md)
