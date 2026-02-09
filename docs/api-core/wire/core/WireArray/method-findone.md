# $wireArray->findOne($selector): Wire|bool

Source: `wire/core/WireArray.php`

Find a single item by selector

This is the same as `WireArray::find()` except that it returns a single
item rather than a new WireArray of items.

## Example

~~~~~
// Get an item with name "foo-bar"
$item = $items->findOne("name=foo-bar");
if($item) {
  // item was found
} else {
  // item was not found
}
~~~~~

## Usage

~~~~~
// basic usage
$wire = $wireArray->findOne($selector);
~~~~~

## Arguments

- `$selector` `string|array|Selectors`

## Return value

- `Wire|bool` Returns item from WireArray or false if the result is empty.

## See Also

- [WireArray::find()](method-find.md)
