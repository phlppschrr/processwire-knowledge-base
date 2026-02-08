# $wireCache->getInfo($verbose = true, $names = array(), $exclude = array(), array $cols = array()): array

Source: `wire/core/WireCache.php`

Get information about all the caches in this WireCache

## Arguments

- `$verbose` (optional) `bool` Whether to be more verbose for human readability
- `$names` (optional) `array|string` Optionally specify name(s) of cache to get info. If omitted, all caches are included.
- `$exclude` (optional) `array|string` Exclude any caches that begin with any of these namespaces (default=[])
- `$cols` (optional) `array` Columns to get, default = [ 'name', 'expires', 'data', 'size' ]

## Return value

array of arrays of cache info
