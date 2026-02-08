# HTMLPurifier_URIFilter

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Chainable filters for custom URI processing.

These filters can perform custom actions on a URI filter object,
including transformation or blacklisting.  A filter named Foo
must have a corresponding configuration directive %URI.Foo,
unless always_load is specified to be true.

The following contexts may be available while URIFilters are being
processed:

     - EmbeddedURI: true if URI is an embedded resource that will
       be loaded automatically on page load
     - CurrentToken: a reference to the token that is currently
       being processed
     - CurrentAttr: the name of the attribute that is currently being
       processed
     - CurrentCSSProperty: the name of the CSS property that is
       currently being processed (if applicable)

@warning This filter is called before scheme object validation occurs.
         Make sure, if you require a specific scheme object, you
         you check that it exists. This allows filters to convert
         proprietary URI schemes into regular ones.

## parse()

Filter a URI object
@param HTMLPurifier_URI $uri Reference to URI object variable
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool Whether or not to continue processing: false indicates
        URL is no good, true indicates continue processing. Note that
        all changes are committed directly on the URI object
/
abstract public function filter(&$uri, $config, $context);
}





/**
Parses a URI into the components and fragment identifier as specified
by RFC 3986.
/
class HTMLPurifier_URIParser
{

/**
Instance of HTMLPurifier_PercentEncoder to do normalization with.
/
protected $percentEncoder;

public function __construct()
{
$this->percentEncoder = new HTMLPurifier_PercentEncoder();
}

/**
Parses a URI.
@param $uri string URI to parse
@return HTMLPurifier_URI representation of URI. This representation has
        not been validated yet and may not conform to RFC.
