# HTMLPurifier_DefinitionCache_Decorator_Memory

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Definition cache decorator class that saves all cache retrievals
to PHP's memory; good for unit tests or circumstances where
there are lots of configuration objects floating around.

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
