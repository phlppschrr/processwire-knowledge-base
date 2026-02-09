# $wireArray->append($item): $this

Source: `wire/core/WireArray.php`

Append an item to the end of the WireArray

This is a functionally identical alias of the `WireArray::add()` method here for
naming consistency with the `WireArray::prepend()` method.

## Example

~~~~~
// Add item to end
$items->append($item);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireArray->append($item);
~~~~~

## Arguments

- `$item` `Wire|WireArray|mixed` Item to append.

## Return value

- `$this` This instance.

## See Also

- [WireArray::prepend()](method-prepend.md)
- [WireArray::add()](method-add.md)
