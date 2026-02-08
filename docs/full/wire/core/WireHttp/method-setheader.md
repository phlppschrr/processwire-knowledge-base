# $wireHttp->setHeader($key, $value): $this

Source: `wire/core/WireHttp.php`

Send an individual request header to send with GET/POST/etc. request

## Usage

~~~~~
// basic usage
$result = $wireHttp->setHeader($key, $value);
~~~~~

## Arguments

- `$key` `string` Header name
- `$value` `string` Header value to set (or specify null to remove header, since 3.0.131)

## Return value

- `$this`
