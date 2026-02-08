# $wireArray->_sort($properties, $numNeeded = null): $this

Source: `wire/core/WireArray.php`

Sort this WireArray by the given properties (internal use)

This function contains additions and modifications by @niklaka.

$properties can be given as a sortByField string, i.e. "name, datestamp" OR as an array of strings, i.e. array("name", "datestamp")
You may also specify the properties as "property.subproperty", where property resolves to a Wire derived object,
and subproperty resolves to a property within that object.

## Usage

~~~~~
// basic usage
$result = $wireArray->_sort($properties);

// usage with all arguments
$result = $wireArray->_sort($properties, $numNeeded = null);
~~~~~

## Arguments

- `$properties` `string|array` Field names to sort by (comma separated string or an array). Prepend or append a minus "-" to reverse the sort (per field).
- `$numNeeded` (optional) `int` *Internal* amount of rows that need to be sorted (optimization used by filterData)

## Return value

- `$this` reference to current instance.
