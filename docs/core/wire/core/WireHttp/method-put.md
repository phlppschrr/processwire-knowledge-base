# WireHttp::put()

Source: `wire/core/WireHttp.php`

Send a PUT request to a URL

“The HTTP PUT request method creates a new resource or replaces a representation of the
target resource with the request payload.”
[More about PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)


@param string $url URL to PUT to (including http:// or https://)

@param array|string $data Associative array of data to send (if not already set before),
  or raw data to send (such as JSON string)

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@since 3.0.222
