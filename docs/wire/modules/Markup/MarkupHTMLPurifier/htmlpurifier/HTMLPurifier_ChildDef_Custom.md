# HTMLPurifier_ChildDef_Custom

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Custom validation class, accepts DTD child definitions

@warning Currently this class is an all or nothing proposition, that is,
         it will only give a bool return value.

## _compileRegex()

Compiles the PCRE regex from a DTD regex ($dtd_regex to $_pcre_regex)

## validateChildren()

@param HTMLPurifier_Node[] $children
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool
