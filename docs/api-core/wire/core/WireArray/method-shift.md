# $wireArray->shift(): Wire|mixed|null

Source: `wire/core/WireArray.php`

Shift an element off the beginning of the WireArray and return it

Consistent with behavior of PHP's `array_shift()` method.

## Usage

~~~~~
// basic usage
$wire = $wireArray->shift();
~~~~~

## Return value

- `Wire|mixed|null` Item shifted off the beginning or NULL if empty.

## See Also

- [WireArray::unshift()](method-unshift.md)
