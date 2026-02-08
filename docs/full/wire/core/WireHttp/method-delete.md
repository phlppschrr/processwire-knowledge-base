# $wireHttp->delete($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a DELETE request to a URL

“The HTTP DELETE request method deletes the specified resource.”
[More about DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)

## Arguments

- `$url` `string` URL to send to (including http:// or https://)
- `$data` (optional) `array|string` Optional associative array of data to send (if not already set before), or raw data to send (such as JSON string)
- `$options` (optional) `array` Optional options to modify default behavior, see the send() method for details.

## Return value

bool|string False on failure or string of contents received on success.

## Since

3.0.222
