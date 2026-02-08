# FieldtypeTextareaHelper

Source: `wire/modules/Fieldtype/FieldtypeTextareaHelper.php`

Helper class for FieldtypeTextarea configuration

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## getConfigInputfields()

Handles field config for Textarea field

@param Field $field

@param InputfieldWrapper $inputfields

@return InputfieldWrapper

@throws WireException

## applyFieldHTML()

Apply all htmlOptions to field values (hook to Session::redirect)

@param HookEvent $event

@throws WireException

## getInputfieldError()

Handle error condition when getInputfield() fails to retrieve requested Inputfield

@param Field $field
