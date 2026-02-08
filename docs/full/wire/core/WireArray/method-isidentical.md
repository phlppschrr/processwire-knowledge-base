# WireArray::isIdentical()

Source: `wire/core/WireArray.php`

Is the given WireArray identical to this one?


@param WireArray $items

@param bool|int $strict Use strict mode? Optionally specify one of the following:
	`true` (boolean): Default. Compares items, item object instances, order, and any other data contained in WireArray.
	`false` (boolean): Compares only that items in the WireArray resolve to the same order and values (though not object instances).

@return bool True if identical, false if not.
