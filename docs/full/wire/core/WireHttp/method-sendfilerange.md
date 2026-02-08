# $wireHttp->sendFileRange($filename, $rangeStr = ''): bool|int

Source: `wire/core/WireHttp.php`

Handle an HTTP_RANGE request for sending of partial file (called by sendFile method)

## Arguments

- `$filename` `string`
- `$rangeStr` (optional) `string` Range string (i.e. `bytes=0-1234`) or omit to pull from `$_SERVER['HTTP_RANGE']`

## Return value

bool|int Returns bytes sent, null if error in request or range, or false if request should be handled by sendFile() instead
