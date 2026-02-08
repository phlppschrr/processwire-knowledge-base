# WireArray::import()

Source: `wire/core/WireArray.php`

Import the given item(s) into this WireArray.

- Adds imported items to the end of the WireArray.
- Skips over any items already present in the WireArray (when duplicateChecking is enabled)


@param array|WireArray $items Items to import.

@return $this

@throws WireException If given items not compatible with the WireArray
