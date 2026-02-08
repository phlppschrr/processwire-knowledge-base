# HTMLPurifier_AttrDef_HTML_LinkTypes

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates a rel/rev link attribute against a directive of allowed values
@note We cannot use Enum because link types allow multiple
      values.
@note Assumes link types are ASCII text

## validate()

@param string $string
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
