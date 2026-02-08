# $pageValues->getInputfield(Page $page, $fieldName): Inputfield|InputfieldWrapper|null

Source: `wire/core/PageValues.php`

Get a single Inputfield for the given field name

- If requested field name refers to a single field, an Inputfield object is returned.
- If requested field name refers to a fieldset or tab, then an InputfieldWrapper representing will be returned.
- Returned Inputfield already has values populated to it.
- Please note this method deals only with custom fields, not system fields name 'name' or 'status', etc.,
  as those are exclusive to the ProcessPageEdit page editor.

## Arguments

- `$fieldName` `string`

## Return value

Inputfield|InputfieldWrapper|null Returns Inputfield, or null if given field name doesn't match field for this page.
