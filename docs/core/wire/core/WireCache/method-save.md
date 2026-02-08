# $wireCache->save($name, $data, $expire = self::expireDaily): bool

Source: `wire/core/WireCache.php`

Save data to cache with given name

~~~~~
$value = "This is the value that will be cached.";

// cache the value, using default expiration (daily)
$cache->save("my-cache-name", $value);

// cache the value, and expire after 1 hour (3600 seconds)
$cache->save("my-cache-name", $value, 3600);
~~~~~

## Arguments

- string $name Name of cache, can be any string up to 255 chars
- string|array|PageArray $data Data that you want to cache. May be string, array of non-object values, or PageArray.
- int|string|Page $expire Lifetime of this cache, in seconds, OR one of the following: - Specify one of the `WireCache::expire*` constants. - Specify the future date you want it to expire (as unix timestamp or any `strtotime()` compatible date format) - Provide a `Page` object to expire when any page using that template is saved. - Specify `WireCache::expireNever` to prevent expiration. - Specify `WireCache::expireSave` to expire when any page or template is saved. - Specify selector string matching pages that–when saved–expire the cache.

## Return value

bool Returns true if cache was successful, false if not

## Throws

- WireException if given data that cannot be cached
