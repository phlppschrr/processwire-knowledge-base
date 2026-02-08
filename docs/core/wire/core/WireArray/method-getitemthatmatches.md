# WireArray::getItemThatMatches()

Source: `wire/core/WireArray.php`

Return the first item in this WireArray having a property named $key with $value, or NULL if not found.

Used internally by get() and has() methods.

@param string $key Property to match.

@param string|int|object $value $value to match.

@return Wire|null
