# InputfieldWrapper::getChildByName()

Source: `wire/core/InputfieldWrapper.php`

Given an Inputfield name, return the child Inputfield or NULL if not found.

This traverses all children recursively to find the requested Inputfield.

This is the same as the `InputfieldWrapper::get()` method except that it can
only return Inputfield or null, and has no crossover with other settings,
properties or API variables.


@param string $name Name of Inputfield

@return Inputfield|InputfieldWrapper|null

@see InputfieldWrapper::get(), InputfieldWrapper::children()
