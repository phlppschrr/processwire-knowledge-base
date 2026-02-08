# HTMLPurifier_AttrDef_CSS_Composite

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Allows multiple validators to attempt to validate attribute.

Composite is just what it sounds like: a composite of many validators.
This means that multiple HTMLPurifier_AttrDef objects will have a whack
at the string.  If one of them passes, that's what is returned.  This is
especially useful for CSS values, which often are a choice between
an enumerated set of predefined values or a flexible data type.

## validate()

@param string $string
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
