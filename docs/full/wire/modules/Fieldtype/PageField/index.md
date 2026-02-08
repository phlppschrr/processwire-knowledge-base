# PageField

Source: `wire/modules/Fieldtype/PageField.php`

Page Field (for FieldtypePage)

Configured with FieldtypePage
==============================

@property int $derefAsPage

@property int|bool $allowUnpub

Configured with InputfieldPage
==============================

@property int $template_id

@property array $template_ids

@property int $parent_id

@property string $inputfield Inputfield class used for input

@property string $labelFieldName Field name to use for label (note: this will be "." if $labelFieldFormat is in use).

@property string $labelFieldFormat Formatting string for $page->getMarkup() as alternative to $labelFieldName

@property string $findPagesCode

@property string $findPagesSelector

@property string $findPagesSelect Same as findPageSelector, but configured interactively with InputfieldSelector.

@property int|bool $addable

@property-read string $inputfieldClass Public property alias of protected getInputfieldClass() method

@property array $inputfieldClasses

@since 3.0.173
