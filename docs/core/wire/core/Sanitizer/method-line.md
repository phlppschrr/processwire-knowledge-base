# Sanitizer::line()

Source: `wire/core/Sanitizer.php`

Sanitize any string of text to single line, no HTML, and no specific max-length (unless given)

This is the same as the text() sanitizer but does not impose a maximum character length (or
byte length) unless given one in the `$maxLength` argument. This is useful in cases where the
text sanitizer’s built in 255 character max length (1020 max bytes) is not enough, or when you
want to specify a max length as part of the method arguments.

Please note that like with the text sanitizer, the max length refers to a maximum number of
characters, not bytes. The maxBytes is automatically set to the maxLength * 4, or can be
specifically set via the `maxBytes` option.


@param string $value String to sanitize

@param int|array $maxLength Maximum length in characters, omit (0) for no max-length, or substitute $options array

@param array $options Options to modify behavior, see text() sanitizer for all options.

@return string

@see Sanitizer::text(), Sanitizer::lines()

@since 3.0.157
