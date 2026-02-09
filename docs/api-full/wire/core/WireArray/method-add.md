# $wireArray->add($item): $this

Source: `wire/core/WireArray.php`

Add an item to the end of the WireArray.

## Example

~~~~~
$items->add($item);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireArray->add($item);
~~~~~

## Arguments

- `$item` `int|string|array|object|Wire|WireArray` Item to add.

## Return value

- `$this`

## Exceptions

- `WireException` If given an item that can't be stored by this WireArray.

## See Also

- [WireArray::prepend()](method-prepend.md)
- [WireArray::append()](method-append.md)
