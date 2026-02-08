# $wireArray->insertBefore($item, $existingItem): $this

Source: `wire/core/WireArray.php`

Insert an item before an existing item

## Example

~~~~~
$items->insertBefore($newItem, $existingItem);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireArray->insertBefore($item, $existingItem);
~~~~~

## Arguments

- `$item` `Wire|string|int` Item you want to insert.
- `$existingItem` `Wire|string|int` Item already present that you want to insert before.

## Return value

- `$this`
