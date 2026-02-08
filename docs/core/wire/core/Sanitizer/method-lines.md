# Sanitizer::lines()

Source: `wire/core/Sanitizer.php`

Sanitize input string as multi-line text, no HTML tags, and no specific max length (unless given)

This is the same as the textarea() sanitizer but does not impose a maximum character length (or
byte length) unless given one in the `$maxLength` argument. This is useful in cases where the
textarea sanitizer’s built in 16kb character max length (64kb max bytes) is not enough, or when you
want to specify a max length as part of the method arguments.

Please note that like with the textarea sanitizer, the max length refers to a maximum number of
characters, not bytes. The maxBytes is automatically set to the maxLength * 4, or can be
specifically set via the `maxBytes` option.


@param string $value String value to sanitize

@param int|array $maxLength Maximum length in characters, omit (0) for no max-length, or substitute $options array

@param array $options Options to modify behavior, see textarea() sanitizer for all options.

@return string

@see Sanitizer::textarea(), Sanitizer::purify(), Sanitizer::line()

@since 3.0.157
