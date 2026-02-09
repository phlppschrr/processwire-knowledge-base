# $wireHttp->put($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a PUT request to a URL

“The HTTP PUT request method creates a new resource or replaces a representation of the
target resource with the request payload.”
[More about PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)

## Usage

~~~~~
// basic usage
$bool = $wireHttp->put($url);

// usage with all arguments
$bool = $wireHttp->put($url, $data = array(), array $options = array());
~~~~~

## Arguments

- `$url` `string` URL to PUT to (including http:// or https://)
- `$data` (optional) `array|string` Associative array of data to send (if not already set before), or raw data to send (such as JSON string)
- `$options` (optional) `array` Optional options to modify default behavior, see the send() method for details.

## Return value

- `bool|string` False on failure or string of contents received on success.

## Since

3.0.222
