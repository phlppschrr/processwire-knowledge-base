# WireHttp::sendFileRange()

Source: `wire/core/WireHttp.php`

Handle an HTTP_RANGE request for sending of partial file (called by sendFile method)

@param string $filename

@param string $rangeStr Range string (i.e. `bytes=0-1234`) or omit to pull from `$_SERVER['HTTP_RANGE']`

@return bool|int Returns bytes sent, null if error in request or range, or false if request should be handled by sendFile() instead
