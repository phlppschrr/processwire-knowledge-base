# $wireArray->getItemThatMatches($key, $value): Wire|null

Source: `wire/core/WireArray.php`

Return the first item in this WireArray having a property named $key with $value, or NULL if not found.

Used internally by get() and has() methods.

## Arguments

- string $key Property to match.
- string|int|object $value $value to match.

## Return value

Wire|null
