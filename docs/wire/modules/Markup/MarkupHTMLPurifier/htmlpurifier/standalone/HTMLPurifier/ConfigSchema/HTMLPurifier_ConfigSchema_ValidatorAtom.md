# HTMLPurifier_ConfigSchema_ValidatorAtom

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/standalone/HTMLPurifier/ConfigSchema/ValidatorAtom.php`

Fluent interface for validating the contents of member variables.
This should be immutable. See HTMLPurifier_ConfigSchema_Validator for
use-cases. We name this an 'atom' because it's ONLY for validations that
are independent and usually scalar.

## assertIsBool()

@return HTMLPurifier_ConfigSchema_ValidatorAtom

## assertIsArray()

@return HTMLPurifier_ConfigSchema_ValidatorAtom

## assertNotNull()

@return HTMLPurifier_ConfigSchema_ValidatorAtom

## assertAlnum()

@return HTMLPurifier_ConfigSchema_ValidatorAtom

## assertNotEmpty()

@return HTMLPurifier_ConfigSchema_ValidatorAtom

## assertIsLookup()

@return HTMLPurifier_ConfigSchema_ValidatorAtom

## error()

@param string $msg
@throws HTMLPurifier_ConfigSchema_Exception
