# $wireInput->httpHostUrl($scheme = null, $httpHost = ''): string

Source: `wire/core/WireInput.php`

Get current scheme and URL for hostname without any path or query string

For example: `https://www.domain.com`

## Arguments

- string|bool|null Optionally specify this argument to force a particular scheme (rather than using current): - boolean true or string "https" to force “https” - boolean false or string "http" to force “http” - string with some other scheme you want to use - blank string or "//" for no scheme, i.e. URL begins with "//" which refers to current scheme. - omit argument or null to use current request scheme (default behavior).
- `$httpHost` (optional) `string` HTTP host to use or leave blank for current host

## Return value

string
