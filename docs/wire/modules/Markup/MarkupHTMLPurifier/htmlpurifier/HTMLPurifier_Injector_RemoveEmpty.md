# HTMLPurifier_Injector_RemoveEmpty

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## prepare()

@type HTMLPurifier_Context
/
private $context;

/**
@type HTMLPurifier_Config
/
private $config;

/**
@type HTMLPurifier_AttrValidator
/
private $attrValidator;

/**
@type bool
/
private $removeNbsp;

/**
@type bool
/
private $removeNbspExceptions;

/**
Cached contents of %AutoFormat.RemoveEmpty.Predicate
@type array
/
private $exclude;

/**
@param HTMLPurifier_Config $config
@param HTMLPurifier_Context $context
@return void

## handleElement()

@param HTMLPurifier_Token $token
