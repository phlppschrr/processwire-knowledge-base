# WireArray::index()

Source: `wire/core/WireArray.php`

Returns a new WireArray of the item at the given index.

Unlike `WireArray::get()` this returns a new WireArray with a single item, or a blank WireArray if item doesn't exist.
Applicable to numerically indexed WireArray only.


@param int $num Index number

@return WireArray

@see WireArray::eq()
