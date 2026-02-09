# $wireArray->getNext($item, $strict = true): Wire|null

Source: `wire/core/WireArray.php`

Given an item, get the item that comes after it in the WireArray

## Usage

~~~~~
// basic usage
$wire = $wireArray->getNext($item);

// usage with all arguments
$wire = $wireArray->getNext($item, $strict = true);
~~~~~

## Arguments

- `$item` `Wire`
- `$strict` (optional) `bool` If false, string comparison will be used rather than exact instance comparison.

## Return value

- `Wire|null` Returns next item if found, or null if not
