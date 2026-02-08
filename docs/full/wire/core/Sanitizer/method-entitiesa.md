# $sanitizer->entitiesA($value, $flags = ENT_QUOTES, $encoding = 'UTF-8', $doubleEncode = true): array|string|int|float|bool

Source: `wire/core/Sanitizer.php`

Entity encode with support for [A]rrays and other non-string values

This is similar to the existing entities() method with the following differences:

- Array values that are strings are encoded recursively to any depth and array is returned.
- Associative array keys (strings) are entity encoded, integer keys are left as-is.
- Objects that implement __toString() are converted to string and entity encoded.
- Objects that do not implement __toString() are converted to a class name.
- If given an int, float, bool, array or string, that is also the type returned.

## Arguments

- `$value` `array|string|int|float|object|bool`
- `$flags` (optional) `int`
- `$encoding` (optional) `string`
- `$doubleEncode` (optional) `bool`

## Return value

array|string|int|float|bool

## See also

- [Sanitizer::entitiesA1()](method-entitiesa1.md)
- [Sanitizer::entities()](method-entities.md)

## Since

3.0.194
