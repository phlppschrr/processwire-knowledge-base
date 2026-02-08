# InputfieldWrapper::import()

Source: `wire/core/InputfieldWrapper.php`

Import the given Inputfield items as children

If given an `InputfieldWrapper`, it will import the children of it and
exclude the wrapper itself. This is different from `InputfieldWrapper::add()`
in that add() would add the wrapper, not just the children. See also
the `InputfieldWrapper::importArray()` method.


@param InputfieldWrapper|array|InputfieldsArray $items Wrapper containing items to add

@return $this

@throws WireException

@see InputfieldWrapper::add(), InputfieldWrapper::importArray()
