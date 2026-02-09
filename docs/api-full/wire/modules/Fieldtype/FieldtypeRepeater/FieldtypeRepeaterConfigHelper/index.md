# FieldtypeRepeaterConfigHelper

Source: `wire/modules/Fieldtype/FieldtypeRepeater/config.php`

Inherits: `Wire`

Class FieldtypeRepeaterConfigHelper

Helper class for configuring repeater fields

Methods:
- [`__construct(Field $field)`](method-__construct.md) Construct
- [`getField(): Field`](method-getfield.md)
- [`isSingleMode(): bool`](method-issinglemode.md)
- [`getConfigInputfields(InputfieldWrapper $inputfields, Template $template, Page $parent): InputfieldWrapper`](method-getconfiginputfields.md) Return configuration fields definable for each FieldtypePage
- [`getConfigInputfieldsStorage(InputfieldWrapper $inputfields): InputfieldFieldset`](method-getconfiginputfieldsstorage.md)
- [`saveConfigInputfields(Template $template)`](method-saveconfiginputfields.md) Helper to getConfigInputfields, handles adding and removing of repeater fields
- [`getConfigAdvancedInputfields(InputfieldWrapper $inputfields)`](method-getconfigadvancedinputfields.md) Advanced config
