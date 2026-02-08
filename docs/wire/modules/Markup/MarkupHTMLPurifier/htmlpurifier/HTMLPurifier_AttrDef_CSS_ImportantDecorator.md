# HTMLPurifier_AttrDef_CSS_ImportantDecorator

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Decorator which enables !important to be used in CSS values.

## validate()

Intercepts and removes !important if necessary
@param string $string
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
