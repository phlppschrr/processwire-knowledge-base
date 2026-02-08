# HTMLPurifier_URIFilter_MakeAbsolute

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## prepare()

@type string
/
public $name = 'MakeAbsolute';

/**
@type
/
protected $base;

/**
@type array
/
protected $basePathStack = array();

/**
@param HTMLPurifier_Config $config
@return bool

## filter()

@param HTMLPurifier_URI $uri
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool

## _collapseStack()

Resolve dots and double-dots in a path stack
@param array $stack
@return array
