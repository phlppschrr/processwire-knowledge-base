# HTMLPurifier_AttrTypes

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Provides lookup array of attribute types to HTMLPurifier_AttrDef objects

## get()

Retrieves a type
@param string $type String type name
@return HTMLPurifier_AttrDef Object AttrDef for type

## set()

Sets a new implementation for a type
@param string $type String type name
@param HTMLPurifier_AttrDef $impl Object AttrDef for type
