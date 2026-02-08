# HTMLPurifier_ElementDef

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Structure that stores an HTML element definition. Used by
HTMLPurifier_HTMLDefinition and HTMLPurifier_HTMLModule.
@note This class is inspected by HTMLPurifier_Printer_HTMLDefinition.
      Please update that class too.
@warning If you add new properties to this class, you MUST update
         the mergeIn() method.

## mergeIn()

Merges the values of another element definition into this one.
Values from the new element def take precedence if a value is
not mergeable.
@param HTMLPurifier_ElementDef $def

## _mergeAssocArray()

Merges one array into another, removes values which equal false
@param $a1 Array by reference that is merged into
@param $a2 Array that merges into $a1
