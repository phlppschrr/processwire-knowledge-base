# $wireArray->stableSort(&$data, $properties, $numNeeded = null): array

Source: `wire/core/WireArray.php`

Sort given array by first given property.

This function contains additions and modifications by @niklaka.

## Usage

~~~~~
// basic usage
$array = $wireArray->stableSort($data, $properties);

// usage with all arguments
$array = $wireArray->stableSort(&$data, $properties, $numNeeded = null);
~~~~~

## Arguments

- array|WireArray &$data Reference to an array to sort.
- `$properties` `array` Array of properties: first property is used now and others in recursion, if needed.
- `$numNeeded` (optional) `int` *Internal* amount of rows that need to be sorted (optimization used by filterData)

## Return value

- `array` Sorted array (at least $numNeeded items, if $numNeeded is given)
