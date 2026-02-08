# $wireArray->findRandom($num): WireArray

Source: `wire/core/WireArray.php`

Find a specified quantity of random elements from this WireArray.

Unlike `WireArray::getRandom()` this method always returns a WireArray (or derived type).

## Example

~~~~~
// Get 3 random items
$randomItems = $items->findRandom(3);
~~~~~

## Usage

~~~~~
// basic usage
$items = $wireArray->findRandom($num);
~~~~~

## Arguments

- `$num` `int` Number of items to return

## Return value

- `WireArray`

## See Also

- [WireArray::getRandom()](method-getrandom.md)
- [WireArray::findRandomTimed()](method-findrandomtimed.md)
