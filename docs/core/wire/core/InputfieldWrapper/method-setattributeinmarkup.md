# InputfieldWrapper::setAttributeInMarkup()

Source: `wire/core/InputfieldWrapper.php`

Set attribute value in markup, optionally replacing a {placeholder} tag

When a placeholder is present in the given $markup, it should be the
attribute name wrapped in `{}`, i.e. `{class}`

Note that class attributes are appended while other attributes are replaced.

@param string $name Attribute name (i.e. "class", "for", etc.)

@param string $value Value to set for the attribute

@param string $markup Markup where the attribute or placeholder exists

@param bool $removeEmpty Remove attribute if it resolves to empty value?

@return string Updated markup

@since 3.0.242
