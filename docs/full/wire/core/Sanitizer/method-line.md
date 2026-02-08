# $sanitizer->line($value, $maxLength = 0, array $options = array()): string

Source: `wire/core/Sanitizer.php`

Sanitize any string of text to single line, no HTML, and no specific max-length (unless given)

This is the same as the text() sanitizer but does not impose a maximum character length (or
byte length) unless given one in the `$maxLength` argument. This is useful in cases where the
text sanitizer’s built in 255 character max length (1020 max bytes) is not enough, or when you
want to specify a max length as part of the method arguments.

Please note that like with the text sanitizer, the max length refers to a maximum number of
characters, not bytes. The maxBytes is automatically set to the maxLength * 4, or can be
specifically set via the `maxBytes` option.

## Arguments

- `$value` `string` String to sanitize
- `$maxLength` (optional) `int|array` Maximum length in characters, omit (0) for no max-length, or substitute $options array
- `$options` (optional) `array` Options to modify behavior, see text() sanitizer for all options.

## Return value

string

## See also

- [Sanitizer::text()](method-text.md)
- [Sanitizer::lines()](method-lines.md)

## Since

3.0.157
