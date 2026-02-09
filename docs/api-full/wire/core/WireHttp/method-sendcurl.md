# $wireHttp->sendCURL($url, $method = 'POST', $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send using CURL

## Usage

~~~~~
// basic usage
$bool = $wireHttp->sendCURL($url);

// usage with all arguments
$bool = $wireHttp->sendCURL($url, $method = 'POST', $options = array());
~~~~~

## Arguments

- `$url` `string`
- `$method` (optional) `string`
- `$options` (optional) `array`

## Return value

- `bool|string`
