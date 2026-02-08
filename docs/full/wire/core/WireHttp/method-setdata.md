# $wireHttp->setData($data): $this

Source: `wire/core/WireHttp.php`

Set an array of data, or string of raw data to send with next GET/POST/etc. request (overwriting the existing data or rawData)

## Usage

~~~~~
// basic usage
$result = $wireHttp->setData($data);
~~~~~

## Arguments

- `$data` `array|string` Associative array of data or string of raw data

## Return value

- `$this`
