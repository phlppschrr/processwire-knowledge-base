# $wireArray->prepend($item): $this

Source: `wire/core/WireArray.php`

Prepend an item to the beginning of the WireArray.

## Example

~~~~~
// Add item to beginning
$items->prepend($item);
~~~~~

## Usage

~~~~~
// basic usage
$result = $wireArray->prepend($item);
~~~~~

## Arguments

- `$item` `Wire|WireArray|mixed` Item to prepend.

## Return value

- `$this` This instance.

## Exceptions

- `WireException`

## See Also

- [WireArray::append()](method-append.md)
