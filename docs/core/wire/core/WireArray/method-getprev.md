# $wireArray->getPrev($item, $strict = true): Wire|null

Source: `wire/core/WireArray.php`

Given an item, get the item before it in the WireArray

## Usage

~~~~~
// basic usage
$wire = $wireArray->getPrev($item);

// usage with all arguments
$wire = $wireArray->getPrev($item, $strict = true);
~~~~~

## Arguments

- `$item` `Wire`
- `$strict` (optional) `bool` If false, string comparison will be used rather than exact instance comparison.

## Return value

- `Wire|null` Returns item that comes before given item, or null if not found
