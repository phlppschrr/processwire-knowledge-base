# WireHttp::head()

Source: `wire/core/WireHttp.php`

Send to a URL using a HEAD request


@param string $url URL to request (including http:// or https://)

@param array|string $data Array of data to send (if not already set before)
  or raw string data to send, such as JSON.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return bool|array False on failure or Array with ResponseHeaders on success.

@see WireHttp::send(), WireHttp::post(), WireHttp::get()
