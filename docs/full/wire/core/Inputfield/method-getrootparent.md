# Inputfield::getRootParent()

Source: `wire/core/Inputfield.php`

Get the root parent InputfieldWrapper element (farthest parent, commonly InputfieldForm)

This returns null only if Inputfield it is called from has not yet been added to an InputfieldWrapper.


@return InputfieldForm|InputfieldWrapper|null

@since 3.0.106
