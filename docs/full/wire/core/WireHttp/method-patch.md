# WireHttp::patch()

Source: `wire/core/WireHttp.php`

Send a PATCH request to a URL

“The HTTP PATCH request method applies partial modifications to a resource.”
[More about PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)


@param string $url URL to PATCH to (including http:// or https://)

@param array|string $data Associative array of data to send (if not already set before),
  or raw data to send (such as JSON string)

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@since 3.0.222
