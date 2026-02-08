# WireArray::iterable($item): bool

Source: `wire/core/WireArray.php`

Determines if the given item iterable as an array.

- Returns true for arrays and WireArray derived objects.
- Can be called statically like this `WireArray::iterable($a)`.

## Arguments

- `$item` `mixed` Item to check for iterability.

## Return value

bool True if item is an iterable array or WireArray (or subclass of WireArray).
