# HTMLPurifier_DefinitionCache_Decorator

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`


## decorate()

Cache object we are decorating
@type HTMLPurifier_DefinitionCache
/
public $cache;

/**
The name of the decorator
@var string
/
public $name;

public function __construct()
{
}

/**
Lazy decorator function
@param HTMLPurifier_DefinitionCache $cache Reference to cache object to decorate
@return HTMLPurifier_DefinitionCache_Decorator

## copy()

Cross-compatible clone substitute
@return HTMLPurifier_DefinitionCache_Decorator

## add()

@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
@return mixed

## set()

@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
@return mixed

## replace()

@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
@return mixed

## get()

@param HTMLPurifier_Config $config
@return mixed

## remove()

@param HTMLPurifier_Config $config
@return mixed

## flush()

@param HTMLPurifier_Config $config
@return mixed

## cleanup()

@param HTMLPurifier_Config $config
@return mixed
