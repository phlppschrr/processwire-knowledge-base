# WireCache::deleteFor()

Source: `wire/core/WireCache.php`

Delete one or more caches in a given namespace

~~~~~
// Delete all in namespace
$cache->deleteFor("my-namespace");

// Delete one cache in namespace
$cache->deleteFor("my-namespace", "my-cache-name");
~~~~~

@param string $ns Namespace of cache.

@param string $name Name of cache. If none specified, all for namespace are deleted.

@return bool True on success, false on failure
