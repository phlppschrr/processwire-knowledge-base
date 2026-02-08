# WireArray::filterData()

Source: `wire/core/WireArray.php`

Filter out Wires that don't match the selector.

This is applicable to and destructive to the WireArray.
This function contains additions and modifications by @niklaka.

@param string|array|Selectors $selectors Selector string|array to use as the filter.

@param bool|int $not Make this a "not" filter? Use int 1 for “not all” mode as if selectors had brackets around it. (default is false)

@return $this reference to current [filtered] instance
