# WireHttp::delete()

Source: `wire/core/WireHttp.php`

Send a DELETE request to a URL

“The HTTP DELETE request method deletes the specified resource.”
[More about DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)


@param string $url URL to send to (including http:// or https://)

@param array|string $data Optional associative array of data to send (if not already set before),
  or raw data to send (such as JSON string)

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|string False on failure or string of contents received on success.

@since 3.0.222
