# $fieldgroup->getPageInputfields(Page $page, $contextStr = '', $fieldName = '', $namespace = '', $flat = true): InputfieldWrapper

Source: `wire/core/Fieldgroup.php`

Get all of the Inputfields for this Fieldgroup associated with the provided Page and populate them.

## Arguments

- `$page` `Page` Page that the Inputfields will be for.
- `$contextStr` (optional) `string|array` Optional context string to append to all the Inputfield names, OR array of options. - Optional context string is helpful for things like repeaters. - Or associative array with any of these options: - `contextStr` (string): Context string to append to all Inputfield names. - `fieldName` (string|array): Limit to particular fieldName(s) or field ID(s). See $fieldName argument for details. - `namespace` (string): Additional namespace for Inputfield context. - `flat` (bool): Return all Inputfields in a flattened InputfieldWrapper? - `populate` (bool): Populate page values to Inputfields? (default=true) since 3.0.208 - `container` (InputfieldWrapper): The InputfieldWrapper element to add fields into, or omit for new. since 3.0.239
- `$fieldName` (optional) `string|array` Limit to a particular fieldName(s) or field IDs (optional). - If specifying a single field (name or ID) and it refers to a fieldset, then all fields in that fieldset will be included. - If specifying an array of field names/IDs the returned InputfieldWrapper will maintain the requested order.
- `$namespace` (optional) `string` Additional namespace for the Inputfield context (optional).
- `$flat` (optional) `bool` Returns all Inputfields in a flattened InputfieldWrapper (default=true).

## Return value

InputfieldWrapper Returns an InputfieldWrapper that acts as a container for multiple Inputfields.
