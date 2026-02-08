# SelectableOptionConfig

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionConfig.php`

Inputfields and processing for Select Options Fieldtype

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## __construct()

Construct

@param Field $field

@param InputfieldWrapper $inputfields

## process()

Custom processing for the options string in getConfigInputfields

Detects and confirms option deletions.

@param Inputfield $inputfield For the _options inputfield

@throws WireException

## getConfigInputfields()

Provides the FieldtypeOptions::getConfigInputfields

@return InputfieldWrapper

@throws WireException
