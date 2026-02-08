# HTMLPurifier_URIFilter_SafeIframe

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Implements safety checks for safe iframes.

@warning This filter is *critical* for ensuring that %HTML.SafeIframe
works safely.

## filter()

@param HTMLPurifier_URI $uri
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool
