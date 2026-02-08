# HTMLPurifier_URI

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

HTML Purifier's internal representation of a URI.
@note
     Internal data-structures are completely escaped. If the data needs
     to be used in a non-URI context (which is very unlikely), be sure
     to decode it first. The URI may not necessarily be well-formed until
     validate() is called.

## getSchemeObj()

Retrieves a scheme object corresponding to the URI's scheme/default
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return HTMLPurifier_URIScheme Scheme object appropriate for validating this URI

## validate()

Generic validation method applicable for all schemes. May modify
this URI in order to get it into a compliant form.
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool True if validation/filtering succeeds, false if failure

## toString()

Convert URI back to string
@return string URI appropriate for output

## isLocal()

Returns true if this URL might be considered a 'local' URL given
the current context.  This is true when the host is null, or
when it matches the host supplied to the configuration.

Note that this does not do any scheme checking, so it is mostly
only appropriate for metadata that doesn't care about protocol
security.  isBenign is probably what you actually want.
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool

## isBenign()

Returns true if this URL should be considered a 'benign' URL,
that is:

     - It is a local URL (isLocal), and
     - It has a equal or better level of security
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool
