# $pageArray->filterData($selectors, $not = false): PageArray|WireArray

Source: `wire/core/PageArray.php`

Filter out Pages that don't match the selector.

This is applicable to and destructive to the WireArray.

## Usage

~~~~~
// basic usage
$items = $pageArray->filterData($selectors);

// usage with all arguments
$items = $pageArray->filterData($selectors, $not = false);
~~~~~

## Arguments

- `$selectors` `string|Selectors|array` Selector string to use as the filter.
- `$not` (optional) `bool|int` Make this a "not" filter? Use int 1 for "not all". (default is false)

## Return value

- `PageArray|WireArray` reference to current [filtered] PageArray
