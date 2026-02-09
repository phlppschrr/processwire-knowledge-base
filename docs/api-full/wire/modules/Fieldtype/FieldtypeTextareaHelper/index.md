# FieldtypeTextareaHelper

Source: `wire/modules/Fieldtype/FieldtypeTextareaHelper.php`

Inherits: `Wire`

## Summary

Helper class for FieldtypeTextarea configuration

Common methods:
- [`getConfigInputfields()`](method-getconfiginputfields.md)
- [`applyFieldHTML()`](method-applyfieldhtml.md)
- [`getInputfieldError()`](method-getinputfielderror.md)

## Methods
- [`getConfigInputfields(Field $field, InputfieldWrapper $inputfields): InputfieldWrapper`](method-getconfiginputfields.md) Handles field config for Textarea field
- [`applyFieldHTML(HookEvent $event)`](method-applyfieldhtml.md) Apply all htmlOptions to field values (hook to Session::redirect)
- [`getInputfieldError(Field $field)`](method-getinputfielderror.md) Handle error condition when getInputfield() fails to retrieve requested Inputfield
