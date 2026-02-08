# HTMLPurifier_AttrDef_CSS_DenyElementDecorator

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Decorator which enables CSS properties to be disabled for specific elements.

## validate()

Checks if CurrentToken is set and equal to $this->element
@param string $string
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
