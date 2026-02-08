# WireArray::stableSort()

Source: `wire/core/WireArray.php`

Sort given array by first given property.

This function contains additions and modifications by @niklaka.

@param array|WireArray &$data Reference to an array to sort.

@param array $properties Array of properties: first property is used now and others in recursion, if needed.

@param int $numNeeded *Internal* amount of rows that need to be sorted (optimization used by filterData)

@return array Sorted array (at least $numNeeded items, if $numNeeded is given)
