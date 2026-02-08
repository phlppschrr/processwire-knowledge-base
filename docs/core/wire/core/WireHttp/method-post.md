# $wireHttp->post($url, $data = array(), array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send a POST request to a URL

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

## Arguments

- string $url URL to post to (including http:// or https://)
- array|string $data Associative array of data to send (if not already set before), or raw string of data to send, such as JSON.
- array $options Optional options to modify default behavior, see the send() method for details.

## Return value

bool|string False on failure or string of contents received on success.

## See also

- [WireHttp::send()](method-___send.md)
- [WireHttp::get()](method-get.md)
- [WireHttp::head()](method-head.md)
