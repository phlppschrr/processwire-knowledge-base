# WireArray::_sort()

Source: `wire/core/WireArray.php`

Sort this WireArray by the given properties (internal use)

This function contains additions and modifications by @niklaka.

$properties can be given as a sortByField string, i.e. "name, datestamp" OR as an array of strings, i.e. array("name", "datestamp")
You may also specify the properties as "property.subproperty", where property resolves to a Wire derived object,
and subproperty resolves to a property within that object.

@param string|array $properties Field names to sort by (comma separated string or an array). Prepend or append a minus "-" to reverse the sort (per field).

@param int $numNeeded *Internal* amount of rows that need to be sorted (optimization used by filterData)

@return $this reference to current instance.
