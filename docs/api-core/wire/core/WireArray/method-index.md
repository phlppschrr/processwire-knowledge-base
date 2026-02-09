# $wireArray->index($num): WireArray

Source: `wire/core/WireArray.php`

Returns a new WireArray of the item at the given index.

Unlike `WireArray::get()` this returns a new WireArray with a single item, or a blank WireArray if item doesn't exist.
Applicable to numerically indexed WireArray only.

## Usage

~~~~~
// basic usage
$items = $wireArray->index($num);
~~~~~

## Arguments

- `$num` `int` Index number

## Return value

- `WireArray`

## See Also

- [WireArray::eq()](method-eq.md)
