# WireHttp::getResponseHeader()

Source: `wire/core/WireHttp.php`

Get the last HTTP response headers (normal array).


Useful to examine for errors if your request returned false
However, the `WireHttp::getResponseHeaders()` (plural) method may be better
and this one is kept primarily for backwards compatibility.

@param string $key Optional header name you want to get

@return array|string|null
