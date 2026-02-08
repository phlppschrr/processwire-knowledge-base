# WireHttp::sendSocket()

Source: `wire/core/WireHttp.php`

Alternate method of sending when allow_url_fopen isn't allowed

@param string $url

@param string $method

@param array $options Optional settings:
	- timeout: number of seconds to timeout

@return bool|string
