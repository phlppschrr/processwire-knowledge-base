# $inputfieldWrapper->getByAttr($attrName, $attrValue): Inputfield|InputfieldWrapper|null

Source: `wire/core/InputfieldWrapper.php`

Given an attribute name and value, return the first matching Inputfield or null if not found

This traverses all children recursively to find the requested Inputfield.

## Arguments

- `$attrName` `string` Attribute to match, such as 'id', 'name', 'value', etc.
- `$attrValue` `string` Attribute value to match

## Return value

Inputfield|InputfieldWrapper|null

## Since

3.0.196
