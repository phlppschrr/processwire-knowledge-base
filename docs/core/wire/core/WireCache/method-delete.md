# $wireCache->delete($name): bool

Source: `wire/core/WireCache.php`

Delete/clear the cache(s) identified by given name or wildcard

~~~~~
// Delete cache named "my-cache-name"
$cache->delete("my-cache-name");

// Delete all caches starting with "my-"
$cache->delete("my-*");
~~~~~

## Arguments

- `$name` `string` Name of cache, or partial name with wildcard (i.e. "MyCache*") to clear multiple caches.

## Return value

bool True on success, false if no cache was cleared
