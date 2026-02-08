# WireArray::_insert()

Source: `wire/core/WireArray.php`

Insert an item either before or after another

Provides the implementation for the insertBefore and insertAfter functions

@param int|string|array|object $item Item you want to insert

@param int|string|array|object $existingItem Item already present that you want to insert before/afer

@param bool $insertBefore True if you want to insert before, false if after

@return $this

@throws WireException if given an invalid item
