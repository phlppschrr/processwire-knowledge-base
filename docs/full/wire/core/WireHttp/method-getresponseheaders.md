# $wireHttp->getResponseHeaders($key = ''): array|string|null

Source: `wire/core/WireHttp.php`

Get the last HTTP response headers (associative array)

All headers are translated to `[key => value]` properties in the array.
The keys are always lowercase and the values are always strings. If you
need multi-value headers, use the `WireHttp::getResponseHeaderValues()` method
instead, which returns multi-value headers as arrays.

This method always returns an associative array of strings, unless you specify the
`$key` option in which case it will return a string, or NULL if the header is not present.

## Arguments

- string $key Optional header name you want to get (if you only need one)

## Return value

array|string|null

## See also

- [WireHttp::getResponseHeaderValues()](method-getresponseheadervalues.md)
