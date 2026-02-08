# $wireArray->add($item): $this

Source: `wire/core/WireArray.php`

Add an item to the end of the WireArray.

~~~~~
$items->add($item);
~~~~~

## Arguments

- int|string|array|object|Wire|WireArray $item Item to add.

## Return value

$this

## Throws

- WireException If given an item that can't be stored by this WireArray.

## See also

- [WireArray::prepend()](method-prepend.md)
- [WireArray::append()](method-append.md)
