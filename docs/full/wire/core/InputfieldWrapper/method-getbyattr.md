# $inputfieldWrapper->getByAttr($attrName, $attrValue): Inputfield|InputfieldWrapper|null

Source: `wire/core/InputfieldWrapper.php`

Given an attribute name and value, return the first matching Inputfield or null if not found

This traverses all children recursively to find the requested Inputfield.

## Arguments

- string $attrName Attribute to match, such as 'id', 'name', 'value', etc.
- string $attrValue Attribute value to match

## Return value

Inputfield|InputfieldWrapper|null

## Meta

- @since 3.0.196
