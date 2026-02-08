# HTMLPurifier_AttrDef_Enum

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates a keyword against a list of valid values.
@warning The case-insensitive compare of this function uses PHP's
         built-in strtolower and ctype_lower functions, which may
         cause problems with international comparisons

## validate()

@param string $string
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string

## make()

@param string $string In form of comma-delimited list of case-insensitive
     valid values. Example: "foo,bar,baz". Prepend "s:" to make
     case sensitive
@return HTMLPurifier_AttrDef_Enum
