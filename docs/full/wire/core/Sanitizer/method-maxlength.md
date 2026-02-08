# Sanitizer::maxLength()

Source: `wire/core/Sanitizer.php`

Limit length of given value to that specified

- For strings, this limits the length to that many characters.
- For arrays, the maxLength is assumed to be the max allowed array items.
- For integers maxLength is assumed to be the max allowed digits.
- For floats, maxLength is assumed to be max allowed digits (including decimal point).
- Returns the same type it is given: string, array, int or float


@param string|int|array|float $value

@param int $maxLength Maximum length (default=128)

@param null|int $maxBytes Maximum allowed bytes (used for string types only)

@return array|float|int|string

@since 3.0.125

@see Sanitizer::minLength()
