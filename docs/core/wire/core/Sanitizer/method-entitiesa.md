# Sanitizer::entitiesA()

Source: `wire/core/Sanitizer.php`

Entity encode with support for [A]rrays and other non-string values

This is similar to the existing entities() method with the following differences:

- Array values that are strings are encoded recursively to any depth and array is returned.
- Associative array keys (strings) are entity encoded, integer keys are left as-is.
- Objects that implement __toString() are converted to string and entity encoded.
- Objects that do not implement __toString() are converted to a class name.
- If given an int, float, bool, array or string, that is also the type returned.


@param array|string|int|float|object|bool $value

@param int $flags

@param string $encoding

@param bool $doubleEncode

@return array|string|int|float|bool

@since 3.0.194

@see Sanitizer::entitiesA1(), Sanitizer::entities()
