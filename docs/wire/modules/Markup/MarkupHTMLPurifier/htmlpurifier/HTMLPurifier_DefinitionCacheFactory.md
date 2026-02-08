# HTMLPurifier_DefinitionCacheFactory

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Responsible for creating definition caches.

## instance()

Retrieves an instance of global definition cache factory.
@param HTMLPurifier_DefinitionCacheFactory $prototype
@return HTMLPurifier_DefinitionCacheFactory

## register()

Registers a new definition cache object
@param string $short Short name of cache object, for reference
@param string $long Full class name of cache object, for construction

## create()

Factory method that creates a cache object based on configuration
@param string $type Name of definitions handled by cache
@param HTMLPurifier_Config $config Config instance
@return mixed

## addDecorator()

Registers a decorator to add to all new cache objects
@param HTMLPurifier_DefinitionCache_Decorator|string $decorator An instance or the name of a decorator
