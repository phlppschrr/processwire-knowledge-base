# HTMLPurifier_URISchemeRegistry

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Registry for retrieving specific URI scheme validator objects.

## getScheme()

Cache of retrieved schemes.
@type HTMLPurifier_URIScheme[]
/
protected $schemes = array();

/**
Retrieves a scheme validator object
@param string $scheme String scheme name like http or mailto
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return HTMLPurifier_URIScheme

## register()

Registers a custom scheme to the cache, bypassing reflection.
@param string $scheme Scheme name
@param HTMLPurifier_URIScheme $scheme_obj
