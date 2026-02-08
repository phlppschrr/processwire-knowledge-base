# $pageValues->getInputfields(Page $page, $fieldName = ''): null|InputfieldWrapper

Source: `wire/core/PageValues.php`

Return all Inputfield objects necessary to edit this page

This method returns an InputfieldWrapper object that contains all the custom Inputfield objects
required to edit this page. You may also specify a `$fieldName` argument to limit what is contained
in the returned InputfieldWrapper.

Please note this method deals only with custom fields, not system fields name 'name' or 'status', etc.,
as those are exclusive to the ProcessPageEdit page editor.

## Arguments

- `$fieldName` (optional) `string|array` Optional field to limit to, typically the name of a fieldset or tab. - Or optionally specify array of $options (See `Fieldgroup::getPageInputfields()` for options).

## Return value

null|InputfieldWrapper Returns an InputfieldWrapper array of Inputfield objects, or NULL on failure.
