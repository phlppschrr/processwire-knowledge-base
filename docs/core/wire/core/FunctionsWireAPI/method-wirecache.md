# $functionsWireAPI->wireCache($name = '', $expire = null, $func = null): WireCache|string|array|PageArray|null

Source: `wire/core/FunctionsWireAPI.php`

Access the $cache API variable as a function

If called with no arguments it returns the $cache API variable.
If called with arguments, it can be used the same as `WireCache::get()`.

## Arguments

- `$name` (optional) `string`
- `$expire` (optional) `callable|int|string|null`
- `$func` (optional) `callable|int|string|null`

## Return value

WireCache|string|array|PageArray|null

## See also

- [WireCache::get()](../WireCache/method-get.md)
