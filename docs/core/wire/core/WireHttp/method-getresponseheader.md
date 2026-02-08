# $wireHttp->getResponseHeader($key = ''): array|string|null

Source: `wire/core/WireHttp.php`

Get the last HTTP response headers (normal array).


Useful to examine for errors if your request returned false
However, the `WireHttp::getResponseHeaders()` (plural) method may be better
and this one is kept primarily for backwards compatibility.

## Usage

~~~~~
// basic usage
$array = $wireHttp->getResponseHeader();

// usage with all arguments
$array = $wireHttp->getResponseHeader($key = '');
~~~~~

## Arguments

- `$key` (optional) `string` Optional header name you want to get

## Return value

- `array|string|null`
