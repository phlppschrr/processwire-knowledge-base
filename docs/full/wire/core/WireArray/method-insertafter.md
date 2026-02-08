# $wireArray->insertAfter($item, $existingItem): $this

Source: `wire/core/WireArray.php`

Insert an item after an existing item

## Example

~~~~~
$items->insertAfter($newItem, $existingItem);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireArray->insertAfter($item, $existingItem);
~~~~~

## Arguments

- `$item` `Wire|string|int` Item you want to insert
- `$existingItem` `Wire|string|int` Item already present that you want to insert after

## Return value

- `$this`
