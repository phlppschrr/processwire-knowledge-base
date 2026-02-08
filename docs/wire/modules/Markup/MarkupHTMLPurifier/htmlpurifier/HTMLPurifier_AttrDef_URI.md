# HTMLPurifier_AttrDef_URI

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Validates a URI as defined by RFC 3986.
@note Scheme-specific mechanics deferred to HTMLPurifier_URIScheme

## make()

@param string $string
@return HTMLPurifier_AttrDef_URI

## validate()

@param string $uri
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool|string
