# HTMLPurifier_URIFilter_Munge

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## prepare()

@type string
/
public $name = 'Munge';

/**
@type bool
/
public $post = true;

/**
@type string
/
private $target;

/**
@type HTMLPurifier_URIParser
/
private $parser;

/**
@type bool
/
private $doEmbed;

/**
@type string
/
private $secretKey;

/**
@type array
/
protected $replace = array();

/**
@param HTMLPurifier_Config $config
@return bool

## filter()

@param HTMLPurifier_URI $uri
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return bool

## makeReplace()

@param HTMLPurifier_URI $uri
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
