# PageField

Source: `wire/modules/Fieldtype/PageField.php`

Inherits: `Field`

Page Field (for FieldtypePage)

## Configured With Fieldtypepage

- `$derefAsPage: int`
- `$allowUnpub: int|bool`

## Configured With Inputfieldpage

- `$template_id: int`
- `$template_ids: array`
- `$parent_id: int`
- `$inputfield: string` Inputfield class used for input
- `$labelFieldName: string` Field name to use for label (note: this will be "." if $labelFieldFormat is in use).
- `$labelFieldFormat: string` Formatting string for $page->getMarkup() as alternative to $labelFieldName
- `$findPagesCode: string`
- `$findPagesSelector: string`
- `$findPagesSelect: string` Same as findPageSelector, but configured interactively with InputfieldSelector.
- `$addable: int|bool`
- `$inputfieldClass: string` Public property alias of protected getInputfieldClass() method
- `$inputfieldClasses: array`

@since 3.0.173
