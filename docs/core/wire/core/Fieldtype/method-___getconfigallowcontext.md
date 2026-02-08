# Fieldtype::___getConfigAllowContext()

Source: `wire/core/Fieldtype.php`

Return an array of configuration field names from that are allowed in fieldgroup/template context

These field names are those that would be used for Inputfields like those returned from getConfigInputfields()
or getConfigArray().

Inputfield field names returned from here are allowed to have unique values per Fieldgroup assignment, rather
than sharing the same setting globally.


@param Field $field

@return array of Inputfield names
