# HTMLPurifier_AttrDef

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Base class for all validating attribute definitions.

This family of classes forms the core for not only HTML attribute validation,
but also any sort of string that needs to be validated or cleaned (which
means CSS properties and composite definitions are defined here too).
Besides defining (through code) what precisely makes the string valid,
subclasses are also responsible for cleaning the code if possible.

## make()

Factory method for creating this class from a string.
@param string $string String construction info
@return HTMLPurifier_AttrDef Created AttrDef object corresponding to $string

## mungeRgb()

Removes spaces from rgb(0, 0, 0) so that shorthand CSS properties work
properly. THIS IS A HACK!
@param string $string a CSS colour definition
@return string

## expandCSSEscape()

Parses a possibly escaped CSS string and returns the "pure"
version of it.
