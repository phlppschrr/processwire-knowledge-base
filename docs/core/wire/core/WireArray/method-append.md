# $wireArray->append($item): $this

Source: `wire/core/WireArray.php`

Append an item to the end of the WireArray

This is a functionally identical alias of the `WireArray::add()` method here for
naming consistency with the `WireArray::prepend()` method.

~~~~~
// Add item to end
$items->append($item);
~~~~~

## Arguments

- Wire|WireArray|mixed $item Item to append.

## Return value

$this This instance.

## See also

- [WireArray::prepend()](method-prepend.md)
- [WireArray::add()](method-add.md)
