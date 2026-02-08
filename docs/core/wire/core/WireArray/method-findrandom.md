# $wireArray->findRandom($num): WireArray

Source: `wire/core/WireArray.php`

Find a specified quantity of random elements from this WireArray.

Unlike `WireArray::getRandom()` this method always returns a WireArray (or derived type).

~~~~~
// Get 3 random items
$randomItems = $items->findRandom(3);
~~~~~

## Arguments

- `$num` `int` Number of items to return

## Return value

WireArray

## See also

- [WireArray::getRandom()](method-getrandom.md)
- [WireArray::findRandomTimed()](method-findrandomtimed.md)
