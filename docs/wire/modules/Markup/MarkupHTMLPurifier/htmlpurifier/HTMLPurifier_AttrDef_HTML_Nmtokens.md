# HTMLPurifier_AttrDef_HTML_Nmtokens

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates contents based on NMTOKENS attribute type.

## split()

Splits a space separated list of tokens into its constituent parts.
@param string $string
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return array

## filter()

Template method for removing certain tokens based on arbitrary criteria.
@note If we wanted to be really functional, we'd do an array_filter
      with a callback. But... we're not.
@param array $tokens
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return array
