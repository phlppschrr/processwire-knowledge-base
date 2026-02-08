# WireCache::getInfo()

Source: `wire/core/WireCache.php`

Get information about all the caches in this WireCache


@param bool $verbose Whether to be more verbose for human readability

@param array|string $names Optionally specify name(s) of cache to get info. If omitted, all caches are included.

@param array|string $exclude Exclude any caches that begin with any of these namespaces (default=[])

@param array $cols Columns to get, default = [ 'name', 'expires', 'data', 'size' ]

@return array of arrays of cache info
