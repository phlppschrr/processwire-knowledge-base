# Sanitizer::bit()

Source: `wire/core/Sanitizer.php`

Sanitize to a bit, returning only integer 0 or 1

This works the same as the bool sanitizer except that it returns 0 or 1 rather than false or true.


@param string|int|array $value

@return int

@see Sanitizer::bool()

@since 3.0.125
