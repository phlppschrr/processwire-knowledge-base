# HTMLPurifier_ConfigSchema_Validator

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/ConfigSchema/Validator.php`

Performs validations on HTMLPurifier_ConfigSchema_Interchange

@note If you see '// handled by InterchangeBuilder', that means a
      design decision in that class would prevent this validation from
      ever being necessary. We have them anyway, however, for
      redundancy.

## validateId()

Validates a HTMLPurifier_ConfigSchema_Interchange_Id object.
@param HTMLPurifier_ConfigSchema_Interchange_Id $id

## validateDirective()

Validates a HTMLPurifier_ConfigSchema_Interchange_Directive object.
@param HTMLPurifier_ConfigSchema_Interchange_Directive $d

## validateDirectiveAllowed()

Extra validation if $allowed member variable of
HTMLPurifier_ConfigSchema_Interchange_Directive is defined.
@param HTMLPurifier_ConfigSchema_Interchange_Directive $d

## validateDirectiveValueAliases()

Extra validation if $valueAliases member variable of
HTMLPurifier_ConfigSchema_Interchange_Directive is defined.
@param HTMLPurifier_ConfigSchema_Interchange_Directive $d

## validateDirectiveAliases()

Extra validation if $aliases member variable of
HTMLPurifier_ConfigSchema_Interchange_Directive is defined.
@param HTMLPurifier_ConfigSchema_Interchange_Directive $d

## with()

Convenience function for generating HTMLPurifier_ConfigSchema_ValidatorAtom
for validating simple member variables of objects.
@param $obj
@param $member
@return HTMLPurifier_ConfigSchema_ValidatorAtom

## error()

Emits an error, providing helpful context.
@throws HTMLPurifier_ConfigSchema_Exception

## getFormattedContext()

Returns a formatted context string.
@return string
