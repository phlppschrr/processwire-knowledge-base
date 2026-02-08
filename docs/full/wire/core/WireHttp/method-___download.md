# WireHttp::___download()

Source: `wire/core/WireHttp.php`

Download a file from a URL and save it locally

First it will attempt to use CURL. If that fails, it will try `fopen()`,
unless you specify the `use` option in `$options`.


@param string $fromURL URL of file you want to download.

@param string $toFile Filename you want to save it to (including full path).

@param array $options Optional options array for PHP's stream_context_create(), plus these optional options:
	- `use` or `useMethod` (string): Specify "curl", "fopen" or "socket" to force a specific method (default=auto-detect).
	- `timeout` (float): Number of seconds till timeout or omit to use previously set timeout setting or default.
 - `fopen_bufferSize' (int): Buffer size (bytes) or 0 to disable buffer, used only by fopen method (default=1048576) 3.0.222+

@return string Filename that was downloaded (including full path).

@throws WireException All error conditions throw exceptions.

@todo update the use option to support array like the send() method
