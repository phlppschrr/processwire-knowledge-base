# $wireArray->filterData($selectors, $not = false): $this

Source: `wire/core/WireArray.php`

Filter out Wires that don't match the selector.

This is applicable to and destructive to the WireArray.
This function contains additions and modifications by @niklaka.

## Arguments

- `$selectors` `string|array|Selectors` Selector string|array to use as the filter.
- `$not` (optional) `bool|int` Make this a "not" filter? Use int 1 for “not all” mode as if selectors had brackets around it. (default is false)

## Return value

$this reference to current [filtered] instance
