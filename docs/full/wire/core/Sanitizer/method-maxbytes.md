# Sanitizer::maxBytes()

Source: `wire/core/Sanitizer.php`

Limit bytes used by given string to max specified

- This function will not break multibyte characters so long as PHP has mb_string.
- This function works only with strings and if given a non-string it will be converted to one.


@param string $value

@param int $maxBytes

@return string

@since 3.0.125
