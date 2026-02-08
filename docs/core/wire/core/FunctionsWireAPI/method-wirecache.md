# FunctionsWireAPI::wireCache()

Source: `wire/core/FunctionsWireAPI.php`

Access the $cache API variable as a function

If called with no arguments it returns the $cache API variable.
If called with arguments, it can be used the same as `WireCache::get()`.

@param string $name

@param callable|int|string|null $expire

@param callable|int|string|null $func

@return WireCache|string|array|PageArray|null

@see WireCache::get()
