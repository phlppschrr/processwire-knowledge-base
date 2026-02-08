# Inputfield::___getConfigAllowContext()

Source: `wire/core/Inputfield.php`

Return a list of config property names allowed for fieldgroup/template context

These should be the names of Inputfields returned by `Inputfield::getConfigInputfields()` or
`Inputfield::getConfigArray()` that are allowed in fieldgroup/template context.

The config property names specified here are allowed to be configured within the context
of a given `Fieldgroup`, enabling the user to configure them independently per template
in the admin.

This is the equivalent to the `Fieldtype::getConfigAllowContext()` method, but for the "Input"
tab rather than the "Details" tab.


@param Field $field

@return array of Inputfield names

@see Fieldtype::getConfigAllowContext()
