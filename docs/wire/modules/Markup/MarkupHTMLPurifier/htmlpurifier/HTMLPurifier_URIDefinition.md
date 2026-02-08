# HTMLPurifier_URIDefinition

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## prepare()

HTMLPurifier_URI object of the base specified at %URI.Base
/
public $base;

/**
String host to consider "home" base, derived off of $base
/
public $host;

/**
Name of default scheme based on %URI.DefaultScheme and %URI.Base
/
public $defaultScheme;

public function __construct()
{
$this->registerFilter(new HTMLPurifier_URIFilter_DisableExternal());
$this->registerFilter(new HTMLPurifier_URIFilter_DisableExternalResources());
$this->registerFilter(new HTMLPurifier_URIFilter_DisableResources());
$this->registerFilter(new HTMLPurifier_URIFilter_HostBlacklist());
$this->registerFilter(new HTMLPurifier_URIFilter_SafeIframe());
$this->registerFilter(new HTMLPurifier_URIFilter_MakeAbsolute());
$this->registerFilter(new HTMLPurifier_URIFilter_Munge());
}

public function registerFilter($filter)
{
$this->registeredFilters[$filter->name] = $filter;
}

public function addFilter($filter, $config)
{
$r = $filter->prepare($config);
if ($r === false) return; // null is ok, for backwards compat
if ($filter->post) {
$this->postFilters[$filter->name] = $filter;
} else {
$this->filters[$filter->name] = $filter;
}
}

protected function doSetup($config)
{
$this->setupMemberVariables($config);
$this->setupFilters($config);
}

protected function setupFilters($config)
{
foreach ($this->registeredFilters as $name => $filter) {
if ($filter->always_load) {
$this->addFilter($filter, $config);
} else {
$conf = $config->get('URI.' . $name);
if ($conf !== false && $conf !== null) {
$this->addFilter($filter, $config);
}
}
}
unset($this->registeredFilters);
}

protected function setupMemberVariables($config)
{
$this->host = $config->get('URI.Host');
$base_uri = $config->get('URI.Base');
if (!is_null($base_uri)) {
$parser = new HTMLPurifier_URIParser();
$this->base = $parser->parse($base_uri);
$this->defaultScheme = $this->base->scheme;
if (is_null($this->host)) $this->host = $this->base->host;
}
if (is_null($this->defaultScheme)) $this->defaultScheme = $config->get('URI.DefaultScheme');
}

public function getDefaultScheme($config, $context)
{
return HTMLPurifier_URISchemeRegistry::instance()->getScheme($this->defaultScheme, $config, $context);
}

public function filter(&$uri, $config, $context)
{
foreach ($this->filters as $name => $f) {
$result = $f->filter($uri, $config, $context);
if (!$result) return false;
}
return true;
}

public function postFilter(&$uri, $config, $context)
{
foreach ($this->postFilters as $name => $f) {
$result = $f->filter($uri, $config, $context);
if (!$result) return false;
}
return true;
}

}





/**
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
/
abstract class HTMLPurifier_URIFilter
{

/**
Unique identifier of filter.
@type string
/
public $name;

/**
True if this filter should be run after scheme validation.
@type bool
/
public $post = false;

/**
True if this filter should always be loaded.
This permits a filter to be named Foo without the corresponding
%URI.Foo directive existing.
@type bool
/
public $always_load = false;

/**
Performs initialization for the filter.  If the filter returns
false, this means that it shouldn't be considered active.
@param HTMLPurifier_Config $config
@return bool
