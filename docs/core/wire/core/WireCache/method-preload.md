# $wireCache->preload(array $names, $expire = null)

Source: `wire/core/WireCache.php`

Preload the given caches, so that they will be returned without query on the next get() call

After a preloaded cache is returned from a get() call, it is removed from local storage.

## Usage

~~~~~
// basic usage
$result = $wireCache->preload($names);

// usage with all arguments
$result = $wireCache->preload(array $names, $expire = null);
~~~~~

## Arguments

- `$names` `array`
- `$expire` (optional) `int|string|null`

## Deprecated
