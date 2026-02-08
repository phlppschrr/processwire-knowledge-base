# HTMLPurifier_TagTransform_Simple

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Simple transformation, just change tag name to something else,
and possibly add some styling. This will cover most of the deprecated
tag cases.

## transform()

@param HTMLPurifier_Token_Tag $tag
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return string
