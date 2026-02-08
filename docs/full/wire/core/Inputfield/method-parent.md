# Inputfield::parent()

Source: `wire/core/Inputfield.php`

Get or set parent of Inputfield

This convenience method performs the same thing as getParent() and setParent().

To get parent, specify no arguments. It will return null if no parent assigned, or an
InputfieldWrapper instance of the parent.

To set parent, specify an InputfieldWrapper for the $parent argument. The return value
is the current Inputfield for fluent interface.


@param null|InputfieldWrapper $parent

@return null|Inputfield|InputfieldWrapper

@since 3.0.110
