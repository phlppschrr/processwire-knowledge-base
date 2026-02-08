# $wireHttp->status($url, $data = array(), $textMode = false, array $options = array()): int|string

Source: `wire/core/WireHttp.php`

Send to a URL using a HEAD request and return the status code

## Arguments

- `$url` `string` URL to request (including http:// or https://)
- `$data` (optional) `mixed` Array of data to send (if not already set before) or raw data
- `$textMode` (optional) `bool` When true function will return a string rather than integer, see the statusText() method.
- `$options` (optional) `array` Optional options to modify default behavior, see the send() method for details.

## Return value

int|string Integer or string of status code (200, 404, etc.)

## See also

- [WireHttp::send()](method-___send.md)
- [WireHttp::statusText()](method-statustext.md)
