# HTMLPurifier_AttrTransform

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Processes an entire attribute array for corrections needing multiple values.

Occasionally, a certain attribute will need to be removed and popped onto
another value.  Instead of creating a complex return syntax for
HTMLPurifier_AttrDef, we just pass the whole attribute array to a
specialized object and have that do the special work.  That is the
family of HTMLPurifier_AttrTransform.

An attribute transformation can be assigned to run before or after
HTMLPurifier_AttrDef validation.  See HTMLPurifier_HTMLDefinition for
more details.

## confiscateAttr()

Retrieves and removes an attribute
@param array &$attr Attribute array to process (passed by reference)
@param mixed $key Key of attribute to confiscate
@return mixed
