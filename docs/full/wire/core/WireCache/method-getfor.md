# WireCache::getFor()

Source: `wire/core/WireCache.php`

Same as get() but with namespace

Namespace is useful to avoid cache name collisions. The ProcessWire core commonly uses cache
namespace to bind cache values to the object class, which often make a good namespace.

Please see the `$cache->get()` method for usage of all arguments.

~~~~~
// specify namespace as a string
$value = $cache->getFor('my-namespace', 'my-cache-name');

// or specify namespace is an object instance
$value = $cache->get($this, 'my-cache-name');
~~~~~

@param string|object $ns Namespace

@param string $name Cache name

@param null|int|string $expire Optional expiration

@param callable|null $func Optional cache generation function

@return string|array|PageArray|mixed|null Returns null if cache doesn’t exist and no generation function provided.

@see WireCache::get()
