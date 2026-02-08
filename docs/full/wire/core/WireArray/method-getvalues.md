# $wireArray->getValues(): array|Wire[]

Source: `wire/core/WireArray.php`

Returns a regular PHP array of all values used in this WireArray.

Unlike the `WireArray::getArray()` method, this does not attempt to maintain original
keys of the items. The returned array is reindexed from 0.

## Usage

~~~~~
// basic usage
$array = $wireArray->getValues();
~~~~~

## Return value

- `array|Wire[]` Values used in the WireArray.

## See Also

- [WireArray::getArray()](method-getarray.md)
