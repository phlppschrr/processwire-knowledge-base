# WireArray::iterable()

Source: `wire/core/WireArray.php`

Determines if the given item iterable as an array.

- Returns true for arrays and WireArray derived objects.
- Can be called statically like this `WireArray::iterable($a)`.


@param mixed $item Item to check for iterability.

@return bool True if item is an iterable array or WireArray (or subclass of WireArray).
