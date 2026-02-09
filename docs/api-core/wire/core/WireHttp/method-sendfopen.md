# $wireHttp->sendFopen($url, $method = 'POST', array $options = array()): bool|string

Source: `wire/core/WireHttp.php`

Send using fopen

## Usage

~~~~~
// basic usage
$bool = $wireHttp->sendFopen($url);

// usage with all arguments
$bool = $wireHttp->sendFopen($url, $method = 'POST', array $options = array());
~~~~~

## Arguments

- `$url` `string`
- `$method` (optional) `string`
- `$options` (optional) `array` Options specific to fopen should be specified in [ 'fopen' => [ ... ] ]

## Return value

- `bool|string`
