# $wireHttp->patch($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a PATCH request to a URL

“The HTTP PATCH request method applies partial modifications to a resource.”
[More about PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)

## Usage

~~~~~
// basic usage
$bool = $wireHttp->patch($url);

// usage with all arguments
$bool = $wireHttp->patch($url, $data = array(), array $options = array());
~~~~~

## Arguments

- `$url` `string` URL to PATCH to (including http:// or https://)
- `$data` (optional) `array|string` Associative array of data to send (if not already set before), or raw data to send (such as JSON string)
- `$options` (optional) `array` Optional options to modify default behavior, see the send() method for details.

## Return value

- `bool|string` False on failure or string of contents received on success.

## Since

3.0.222
