# InputfieldWrapper::getByAttr()

Source: `wire/core/InputfieldWrapper.php`

Given an attribute name and value, return the first matching Inputfield or null if not found

This traverses all children recursively to find the requested Inputfield.


@param string $attrName Attribute to match, such as 'id', 'name', 'value', etc.

@param string $attrValue Attribute value to match

@return Inputfield|InputfieldWrapper|null

@since 3.0.196
