# HTMLPurifier_DefinitionCache

Source: `wire/modules/Markup/MarkupHTMLPurifier/htmlpurifier/HTMLPurifier.standalone.php`

Abstract class representing Definition cache managers that implements
useful common methods and is a factory.
@todo Create a separate maintenance file advanced users can use to
      cache their custom HTMLDefinition, which can be loaded
      via a configuration directive
@todo Implement memcached

## generateKey()

Generates a unique identifier for a particular configuration
@param HTMLPurifier_Config $config Instance of HTMLPurifier_Config
@return string

## isOld()

Tests whether or not a key is old with respect to the configuration's
version and revision number.
@param string $key Key to test
@param HTMLPurifier_Config $config Instance of HTMLPurifier_Config to test against
@return bool

## checkDefType()

Checks if a definition's type jives with the cache's type
@note Throws an error on failure
@param HTMLPurifier_Definition $def Definition object to check
@return bool true if good, false if not

## setup()

Adds a definition object to the cache
@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
/
abstract public function add($def, $config);

/**
Unconditionally saves a definition object to the cache
@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
/
abstract public function set($def, $config);

/**
Replace an object in the cache
@param HTMLPurifier_Definition $def
@param HTMLPurifier_Config $config
/
abstract public function replace($def, $config);

/**
Retrieves a definition object from the cache
@param HTMLPurifier_Config $config
/
abstract public function get($config);

/**
Removes a definition object to the cache
@param HTMLPurifier_Config $config
/
abstract public function remove($config);

/**
Clears all objects from cache
@param HTMLPurifier_Config $config
/
abstract public function flush($config);

/**
Clears all expired (older version or revision) objects from cache
@note Be careful implementing this method as flush. Flush must
      not interfere with other Definition types, and cleanup()
      should not be repeatedly called by userland code.
@param HTMLPurifier_Config $config
/
abstract public function cleanup($config);
}





/**
Responsible for creating definition caches.
/
class HTMLPurifier_DefinitionCacheFactory
{
/**
@type array
/
protected $caches = array('Serializer' => array());

/**
@type array
/
protected $implementations = array();

/**
@type HTMLPurifier_DefinitionCache_Decorator[]
/
protected $decorators = array();

/**
Initialize default decorators
