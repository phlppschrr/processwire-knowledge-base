# $wireCache->deleteFor($ns, $name = ''): bool

Source: `wire/core/WireCache.php`

Delete one or more caches in a given namespace

## Example

~~~~~
// Delete all in namespace
$cache->deleteFor("my-namespace");

// Delete one cache in namespace
$cache->deleteFor("my-namespace", "my-cache-name");
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wireCache->deleteFor($ns);

// usage with all arguments
$bool = $wireCache->deleteFor($ns, $name = '');
~~~~~

## Arguments

- `$ns` `string` Namespace of cache.
- `$name` (optional) `string` Name of cache. If none specified, all for namespace are deleted.

## Return value

- `bool` True on success, false on failure
