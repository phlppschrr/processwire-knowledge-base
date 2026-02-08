# $processWire->___finished(array $data = array())

Source: `wire/core/ProcessWire.php`

Hookable ready for anyone that wants to hook when the request is finished

## Usage

~~~~~
// basic usage
$result = $processWire->___finished();

// usage with all arguments
$result = $processWire->___finished(array $data = array());
~~~~~

## Arguments

- `$data` (optional) `array` Additional data for hooks (3.0.147+ only): - `maintenance` (bool): Allow maintenance to run? (default=true) - `prevStatus` (int): Previous status before finished status (render, download or failed). - `exited` (bool): True if request was exited before finished (ProcessWire instance destructed before expected). 3.0.180+ - `redirectUrl` (string): Contains redirect URL only if request ending with redirect (not present otherwise). - `redirectType` (int): Contains redirect type 301 or 302, only if requestUrl property is also present.
