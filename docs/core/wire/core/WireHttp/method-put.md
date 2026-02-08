# $wireHttp->put($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a PUT request to a URL

“The HTTP PUT request method creates a new resource or replaces a representation of the
target resource with the request payload.”
[More about PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)

## Arguments

- string $url URL to PUT to (including http:// or https://)
- array|string $data Associative array of data to send (if not already set before), or raw data to send (such as JSON string)
- array $options Optional options to modify default behavior, see the send() method for details.

## Return value

bool|string False on failure or string of contents received on success.

## Meta

- @since 3.0.222
