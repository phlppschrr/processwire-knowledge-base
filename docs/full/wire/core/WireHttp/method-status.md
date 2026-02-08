# WireHttp::status()

Source: `wire/core/WireHttp.php`

Send to a URL using a HEAD request and return the status code


@param string $url URL to request (including http:// or https://)

@param mixed $data Array of data to send (if not already set before) or raw data

@param bool $textMode When true function will return a string rather than integer, see the statusText() method.

@param array $options Optional options to modify default behavior, see the send() method for details.

@return int|string Integer or string of status code (200, 404, etc.)

@see WireHttp::send(), WireHttp::statusText()
