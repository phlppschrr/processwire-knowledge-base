# $functionsAPI->cache($name = '', $expire = null, $func = null): WireCache|string|array|PageArray|null

Source: `wire/core/FunctionsAPI.php`

Get and save caches ($cache API variable as a function)

This behaves the same as the $cache API variable but does support arguments as a
shortcut for the `$cache->get()` method.

- If called with no arguments it returns the $cache API variable.
- If called with arguments, it can be used the same as `WireCache::get()`.

## Usage

~~~~~
// basic usage
$wireCache = $functionsAPI->cache();

// usage with all arguments
$wireCache = $functionsAPI->cache($name = '', $expire = null, $func = null);
~~~~~

## Arguments

- `$name` (optional) `string`
- `$expire` (optional) `callable|int|string|null`
- `$func` (optional) `callable|int|string|null`

## Return value

- `WireCache|string|array|PageArray|null`

## See Also

- WireCache
- [WireCache::get()](../WireCache/method-get.md)
