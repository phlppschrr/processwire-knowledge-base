# $wireCache->saveFor($ns, $name, $data, $expire = self::expireDaily): bool

Source: `wire/core/WireCache.php`

Same as save() except with namespace

Namespace is useful to avoid cache name collisions. The ProcessWire core commonly uses cache
namespace to bind cache values to the object class, which often make a good namespace.

~~~~~
// save cache using manually specified namespace
$cache->save("my-namespace", "my-cache-name", $value);

// save cache using namespace of current object
$cache->save($this, "my-cache-name", $value);
~~~~~

## Arguments

- `$ns` `string|object` Namespace for cache
- `$name` `string` Name of cache, can be any string up to 255 chars
- `$data` `string|array|PageArray` Data that you want to cache
- `$expire` (optional) `int|Page` Lifetime of this cache, in seconds, OR one of the following: - Specify one of the `WireCache::expire*` constants. - Specify the future date you want it to expire (as unix timestamp or any strtotime compatible date format) - Provide a `Page` object to expire when any page using that template is saved. - Specify `WireCache::expireNever` to prevent expiration. - Specify `WireCache::expireSave` to expire when any page or template is saved. - Specify selector string matching pages that, when saved, expire the cache.

## Return value

bool Returns true if cache was successful, false if not
