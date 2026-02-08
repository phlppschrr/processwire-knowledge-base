# $wireArray->replace($itemA, $itemB): $this

Source: `wire/core/WireArray.php`

Replace one item with the other

- The order of the arguments does not matter.
- If both items are already present, they will change places.
- If one item is not already present, it will replace the one that is.
- If neither item is present, both will be added at the end.

## Example

~~~~~
$items->replace($existingItem, $newItem);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireArray->replace($itemA, $itemB);
~~~~~

## Arguments

- `$itemA` `Wire|string|int`
- `$itemB` `Wire|string|int`

## Return value

- `$this`
