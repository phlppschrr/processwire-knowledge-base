# HTMLPurifier_ContentSets

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

@todo Unit test

## generateChildDef()

Accepts a definition; generates and assigns a ChildDef for it
@param HTMLPurifier_ElementDef $def HTMLPurifier_ElementDef reference
@param HTMLPurifier_HTMLModule $module Module that defined the ElementDef

## getChildDef()

Instantiates a ChildDef based on content_model and content_model_type
member variables in HTMLPurifier_ElementDef
@note This will also defer to modules for custom HTMLPurifier_ChildDef
      subclasses that need content set expansion
@param HTMLPurifier_ElementDef $def HTMLPurifier_ElementDef to have ChildDef extracted
@param HTMLPurifier_HTMLModule $module Module that defined the ElementDef
@return HTMLPurifier_ChildDef corresponding to ElementDef

## convertToLookup()

Converts a string list of elements separated by pipes into
a lookup array.
@param string $string List of elements
@return array Lookup array of elements
