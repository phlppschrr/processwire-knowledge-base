# $wireHttp->get($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a GET request to URL

~~~~~
$http = new WireHttp();
$response = $http->get("http://domain.com/path/", [
  'foo' => 'bar',
]);
if($response !== false) {
  echo "Successful response: " . $sanitizer->entities($response);
} else {
  echo "HTTP request failed: " . $http->getError();
}
~~~~~

## Arguments

- string $url URL to send request to (including http:// or https://)
- array|string $data Array of data to send (if not already set before) or raw string of data to send, such as JSON.
- array $options Optional options to modify default behavior, see the send() method for details.

## Return value

bool|string False on failure or string of contents received on success.

## See also

- [WireHttp::send()](method-___send.md)
- [WireHttp::post()](method-post.md)
- [WireHttp::head()](method-head.md)
- [WireHttp::getJSON()](index.md)
