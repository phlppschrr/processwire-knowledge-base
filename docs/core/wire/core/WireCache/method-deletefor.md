# $wireCache->deleteFor($ns, $name = ''): bool

Source: `wire/core/WireCache.php`

Delete one or more caches in a given namespace

~~~~~
// Delete all in namespace
$cache->deleteFor("my-namespace");

// Delete one cache in namespace
$cache->deleteFor("my-namespace", "my-cache-name");
~~~~~

## Arguments

- string $ns Namespace of cache.
- string $name Name of cache. If none specified, all for namespace are deleted.

## Return value

bool True on success, false on failure
