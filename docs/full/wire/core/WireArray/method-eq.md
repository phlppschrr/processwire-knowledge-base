# WireArray::eq()

Source: `wire/core/WireArray.php`

Returns the item at the given index starting from 0, or NULL if it doesn't exist.

Unlike the `WireArray::index()` method, this returns an actual item and not another WireArray.


@param int $num Return the n'th item in this WireArray. Specify a negative number to count from the end rather than the start.

@return Wire|null

@see WireArray::index()
