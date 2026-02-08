# FieldtypeRepeaterConfigHelper

Source: `wire/modules/Fieldtype/FieldtypeRepeater/config.php`

Class FieldtypeRepeaterConfigHelper

Helper class for configuring repeater fields

## __construct()

Construct

@param Field $field

## getField()

@return Field

@since 3.0.188

## isSingleMode()

@return bool

## getConfigInputfields()

Return configuration fields definable for each FieldtypePage

@param InputfieldWrapper $inputfields

@param Template $template

@param Page $parent

@return InputfieldWrapper

## getConfigInputfieldsStorage()

@param InputfieldWrapper $inputfields

@return InputfieldFieldset

## saveConfigInputfields()

Helper to getConfigInputfields, handles adding and removing of repeater fields

@param Template $template

@throws WireException

## getConfigAdvancedInputfields()

Advanced config

@param InputfieldWrapper $inputfields
