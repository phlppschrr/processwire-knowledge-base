# $wireHttp->sendSocket($url, $method = 'POST', $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Alternate method of sending when allow_url_fopen isn't allowed

## Usage

~~~~~
// basic usage
$bool = $wireHttp->sendSocket($url);

// usage with all arguments
$bool = $wireHttp->sendSocket($url, $method = 'POST', $options = array());
~~~~~

## Arguments

- `$url` `string`
- `$method` (optional) `string`
- `$options` (optional) `array` Optional settings: - timeout: number of seconds to timeout

## Return value

- `bool|string`
