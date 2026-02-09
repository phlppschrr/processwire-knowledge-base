# $wireHttp->getUserAgent(): string

Source: `wire/core/WireHttp.php`

Get the current user-agent header

To set the user agent header, use `$http->setHeader('user-agent', '...');`
or in 3.0.183+ there is also `$http->setUserAgent('...');`

## Usage

~~~~~
// basic usage
$string = $wireHttp->getUserAgent();
~~~~~

## Return value

- `string`
