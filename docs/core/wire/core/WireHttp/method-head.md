# $wireHttp->head($url, $data = array(), array $options = array()): bool|array

Source: `wire/core/WireHttp.php`

Send to a URL using a HEAD request

## Arguments

- string $url URL to request (including http:// or https://)
- array|string $data Array of data to send (if not already set before) or raw string data to send, such as JSON.
- array $options Optional options to modify default behavior, see the send() method for details.

## Return value

bool|array False on failure or Array with ResponseHeaders on success.

## See also

- [WireHttp::send()](method-___send.md)
- [WireHttp::post()](method-post.md)
- [WireHttp::get()](method-get.md)
