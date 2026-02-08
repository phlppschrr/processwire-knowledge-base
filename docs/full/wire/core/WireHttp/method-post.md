# WireHttp::post()

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


@param string $url URL to post to (including http:// or https://)

@param array|string $data Associative array of data to send (if not already set before),
  or raw string of data to send, such as JSON.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@see WireHttp::send(), WireHttp::get(), WireHttp::head()
