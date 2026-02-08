# WireHttp::get()

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


@param string $url URL to send request to (including http:// or https://)

@param array|string $data Array of data to send (if not already set before)
  or raw string of data to send, such as JSON.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@see WireHttp::send(), WireHttp::post(), WireHttp::head(), WireHttp::getJSON()
