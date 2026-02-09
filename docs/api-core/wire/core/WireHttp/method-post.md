# $wireHttp->post($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a POST request to a URL

## Example

~~~~~
$http = new WireHttp();
$response = $http->post("http://domain.com/path/", [
  'foo' => 'bar',
]);
if($response !== false) {
  echo "Successful response: " . $sanitizer->entities($response);
} else {
  echo "HTTP request failed: " . $http->getError();
}
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wireHttp->post($url);

// usage with all arguments
$bool = $wireHttp->post($url, $data = array(), array $options = array());
~~~~~

## Arguments

- `$url` `string` URL to post to (including http:// or https://)
- `$data` (optional) `array|string` Associative array of data to send (if not already set before), or raw string of data to send, such as JSON.
- `$options` (optional) `array` Optional options to modify default behavior, see the send() method for details.

## Return value

- `bool|string` False on failure or string of contents received on success.

## See Also

- [WireHttp::send()](method-___send.md)
- [WireHttp::get()](method-get.md)
- [WireHttp::head()](method-head.md)
