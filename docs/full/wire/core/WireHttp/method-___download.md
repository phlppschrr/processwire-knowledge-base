# $wireHttp->___download($fromURL, $toFile, array $options = array()): string

Source: `wire/core/WireHttp.php`

Download a file from a URL and save it locally

First it will attempt to use CURL. If that fails, it will try `fopen()`,
unless you specify the `use` option in `$options`.

## Usage

~~~~~
// basic usage
$string = $wireHttp->___download($fromURL, $toFile);

// usage with all arguments
$string = $wireHttp->___download($fromURL, $toFile, array $options = array());
~~~~~

## Arguments

- `$fromURL` `string` URL of file you want to download.
- `$toFile` `string` Filename you want to save it to (including full path).
- `$options` (optional) `array` Optional options array for PHP's stream_context_create(), plus these optional options: - `use` or `useMethod` (string): Specify "curl", "fopen" or "socket" to force a specific method (default=auto-detect). - `timeout` (float): Number of seconds till timeout or omit to use previously set timeout setting or default. - `fopen_bufferSize' (int): Buffer size (bytes) or 0 to disable buffer, used only by fopen method (default=1048576) 3.0.222+

## Return value

- `string` Filename that was downloaded (including full path).

## Exceptions

- `WireException` All error conditions throw exceptions.

## Details

- @todo update the use option to support array like the send() method
