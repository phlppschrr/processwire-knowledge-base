# InputfieldWrapper::getValueByName()

Source: `wire/core/InputfieldWrapper.php`

Get value of Inputfield by name

This traverses all children recursively to find the requested Inputfield,
and get the value attribute from it. A value of null is returned if the
Inputfield cannot be found.

@param string $name

@return array|float|int|object|Wire|WireArray|WireData|string|null

@since 3.0.172
