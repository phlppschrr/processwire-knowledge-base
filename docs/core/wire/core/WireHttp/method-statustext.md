# $wireHttp->statusText($url, $data = array(), array $options = array()): string

Source: `wire/core/WireHttp.php`

Send to a URL using HEAD and return the status code and text like "200 OK"

## Arguments

- `$url` `string` URL to request (including http:// or https://)
- `$data` (optional) `mixed` Array of data to send (if not already set before) or raw data
- `$options` (optional) `array` Optional options to modify default behavior, see the send() method for details.

## Return value

string String of status code + text on success. Example: "200 OK', "302 Found", "404 Not Found"

## See also

- [WireHttp::send()](method-___send.md)
- [WireHttp::status()](method-status.md)
