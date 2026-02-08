# WireHttp::statusText()

Source: `wire/core/WireHttp.php`

Send to a URL using HEAD and return the status code and text like "200 OK"


@param string $url URL to request (including http:// or https://)

@param mixed $data Array of data to send (if not already set before) or raw data

@param array $options Optional options to modify default behavior, see the send() method for details.

@return string String of status code + text on success.
	Example: "200 OK', "302 Found", "404 Not Found"

@see WireHttp::send(), WireHttp::status()
