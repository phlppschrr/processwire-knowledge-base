# $wireHttp->setHeaders(array $headers, array $options = array()): $this

Source: `wire/core/WireHttp.php`

Set an array of request headers to send with GET/POST/etc. request

Merges with existing headers unless you specify true for the $reset option (since 3.0.131).
If you specify null for any header value, it removes the header (since 3.0.131).

## Arguments

- `$headers` `array` Associative array of headers to set
- `$options` (optional) `array` Options to modify default behavior (since 3.0.131): - `reset` (bool): Reset/clear all existing headers first? (default=false) - `replacements` (array): Associative array of [ find => replace ] values to replace in header values (default=[])

## Return value

$this
