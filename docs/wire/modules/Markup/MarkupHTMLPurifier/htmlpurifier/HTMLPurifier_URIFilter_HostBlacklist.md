# HTMLPurifier_URIFilter_HostBlacklist

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## prepare()

@type string
/
public $name = 'HostBlacklist';

/**
@type array
/
protected $blacklist = array();

/**
@param HTMLPurifier_Config $config
@return bool

## filter()

@param HTMLPurifier_URI $uri
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool
