# HTMLPurifier_AttrDef_Clone

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Dummy AttrDef that mimics another AttrDef, BUT it generates clones
with make.

## validate()

@param string $v
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string

## make()

@param string $string
@return HTMLPurifier_AttrDef
