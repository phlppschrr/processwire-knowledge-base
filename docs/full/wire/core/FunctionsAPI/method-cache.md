# FunctionsAPI::cache()

Source: `wire/core/FunctionsAPI.php`

Get and save caches ($cache API variable as a function)

This behaves the same as the $cache API variable but does support arguments as a
shortcut for the `$cache->get()` method.

- If called with no arguments it returns the $cache API variable.
- If called with arguments, it can be used the same as `WireCache::get()`.


@param string $name

@param callable|int|string|null $expire

@param callable|int|string|null $func

@return WireCache|string|array|PageArray|null

@see WireCache, WireCache::get()
