# HTMLPurifier_AttrDef_CSS_Number

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates a number as defined by the CSS spec.

## validate()

@param string $number
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return string|bool
@warning Some contexts do not pass $config, $context. These
         variables should not be used without checking HTMLPurifier_Length
