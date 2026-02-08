# $wireArray->unshift($item): $this

Source: `wire/core/WireArray.php`

Unshift an element to the beginning of the WireArray (alias for prepend)

This is for consistency with PHP's naming convention of the `array_unshift()` method.

## Usage

~~~~~
// basic usage
$result = $wireArray->unshift($item);
~~~~~

## Arguments

- `$item` `Wire|WireArray|mixed` Item to prepend.

## Return value

- `$this` This instance.

## See Also

- [WireArray::shift()](method-shift.md)
- [WireArray::prepend()](method-prepend.md)
