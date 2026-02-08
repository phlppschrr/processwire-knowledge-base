# HTMLPurifier_AttrDef_Integer

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates an integer.
@note While this class was modeled off the CSS definition, no currently
      allowed CSS uses this type.  The properties that do are: widows,
      orphans, z-index, counter-increment, counter-reset.  Some of the
      HTML attributes, however, find use for a non-negative version of this.

## validate()

@param string $integer
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
