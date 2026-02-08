# $inputfieldWrapper->import($items): $this

Source: `wire/core/InputfieldWrapper.php`

Import the given Inputfield items as children

If given an `InputfieldWrapper`, it will import the children of it and
exclude the wrapper itself. This is different from `InputfieldWrapper::add()`
in that add() would add the wrapper, not just the children. See also
the `InputfieldWrapper::importArray()` method.

## Arguments

- `$items` `InputfieldWrapper|array|InputfieldsArray` Wrapper containing items to add

## Return value

$this

## Throws

- WireException

## See also

- [InputfieldWrapper::add()](method-add.md)
- [InputfieldWrapper::importArray()](method-importarray.md)
