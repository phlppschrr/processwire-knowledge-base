# HTMLPurifier_VarParser

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Parses string representations into their corresponding native PHP
variable type. The base implementation does a simple type-check.

## error()

Throws an exception.
@throws HTMLPurifier_VarParserException

## errorInconsistent()

Throws an inconsistency exception.
@note This should not ever be called. It would be called if we
      extend the allowed values of HTMLPurifier_VarParser without
      updating subclasses.
@param string $class
@param int $type
@throws HTMLPurifier_Exception

## errorGeneric()

Generic error for if a type didn't work.
@param mixed $var
@param int $type

## getTypeName()

@param int $type
@return string
