# $wireArray->index($num): WireArray

Source: `wire/core/WireArray.php`

Returns a new WireArray of the item at the given index.

Unlike `WireArray::get()` this returns a new WireArray with a single item, or a blank WireArray if item doesn't exist.
Applicable to numerically indexed WireArray only.

## Arguments

- int $num Index number

## Return value

WireArray

## See also

- [WireArray::eq()](method-eq.md)
