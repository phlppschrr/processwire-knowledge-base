# PageArray::filterData()

Source: `wire/core/PageArray.php`

Filter out Pages that don't match the selector.

This is applicable to and destructive to the WireArray.

@param string|Selectors|array $selectors Selector string to use as the filter.

@param bool|int $not Make this a "not" filter? Use int 1 for "not all". (default is false)

@return PageArray|WireArray reference to current [filtered] PageArray
