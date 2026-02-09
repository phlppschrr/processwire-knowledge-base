# $wireCache->preloadFor($ns, $expire = null)

Source: `wire/core/WireCache.php`

Preload all caches for the given object or namespace

## Usage

~~~~~
// basic usage
$result = $wireCache->preloadFor($ns);

// usage with all arguments
$result = $wireCache->preloadFor($ns, $expire = null);
~~~~~

## Arguments

- `$ns` `object|string`
- `$expire` (optional) `int|string|null`

## Deprecated
