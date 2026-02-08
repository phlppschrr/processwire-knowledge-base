# WireCache::renderCacheValue()

Source: `wire/core/WireCache.php`

Render and save a cache value, when given a function to do so

Provided $func may specify any arguments that correspond with the names of API vars
and it will be sent those arguments.

Provided $func may either echo or return it's output. If any value is returned by
the function it will be used as the cache value. If no value is returned, then
the output buffer will be used as the cache value.

@param string $name

@param int|string|null $expire

@param callable $func

@return bool|string

@since 2.5.28
