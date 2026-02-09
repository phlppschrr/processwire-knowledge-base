# $wireCache->getFor($ns, $name, $expire = null, $func = null): string|array|PageArray|mixed|null

Source: `wire/core/WireCache.php`

Same as get() but with namespace

Namespace is useful to avoid cache name collisions. The ProcessWire core commonly uses cache
namespace to bind cache values to the object class, which often make a good namespace.

Please see the `$cache->get()` method for usage of all arguments.

## Example

~~~~~
// specify namespace as a string
$value = $cache->getFor('my-namespace', 'my-cache-name');

// or specify namespace is an object instance
$value = $cache->get($this, 'my-cache-name');
~~~~~

## Usage

~~~~~
// basic usage
$string = $wireCache->getFor($ns, $name);

// usage with all arguments
$string = $wireCache->getFor($ns, $name, $expire = null, $func = null);
~~~~~

## Arguments

- `$ns` `string|object` Namespace
- `$name` `string` Cache name
- `$expire` (optional) `null|int|string` Optional expiration
- `$func` (optional) `callable|null` Optional cache generation function

## Return value

- `string|array|PageArray|mixed|null` Returns null if cache doesn’t exist and no generation function provided.

## See Also

- [WireCache::get()](method-get.md)
