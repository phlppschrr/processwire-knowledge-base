# $wireArray->getRandom($num = 1, $alwaysArray = false): WireArray|Wire|mixed|null

Source: `wire/core/WireArray.php`

Get a random item from this WireArray.

- If one item is requested (default), the item is returned (unless `$alwaysArray` argument is true).
- If multiple items are requested, a new `WireArray` of those items is returned.
- We recommend using this method when you just need 1 random item, and using the `WireArray::findRandom()` method
  when you need multiple random items.

## Example

~~~~~
// Get a single random item
$randomItem = $items->getRandom();

// Get 3 random items
$randomItems = $items->getRandom(3);
~~~~~

## Usage

~~~~~
// basic usage
$items = $wireArray->getRandom();

// usage with all arguments
$items = $wireArray->getRandom($num = 1, $alwaysArray = false);
~~~~~

## Arguments

- `$num` (optional) `int` Number of items to return. Optional and defaults to 1.
- `$alwaysArray` (optional) `bool` If true, then method will always return an array of items, even if it only contains 1 item.

## Return value

- `WireArray|Wire|mixed|null` Returns value of item, or new WireArray of items if more than one requested.

## See Also

- [WireArray::findRandom()](method-findrandom.md)
- [WireArray::findRandomTimed()](method-findrandomtimed.md)
