# $wireHttp->patch($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a PATCH request to a URL

“The HTTP PATCH request method applies partial modifications to a resource.”
[More about PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)

## Arguments

- string $url URL to PATCH to (including http:// or https://)
- array|string $data Associative array of data to send (if not already set before), or raw data to send (such as JSON string)
- array $options Optional options to modify default behavior, see the send() method for details.

## Return value

bool|string False on failure or string of contents received on success.

## Meta

- @since 3.0.222
