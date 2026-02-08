# $session->setCookie($name, $value, $expires = 0, $path = '/', $domain = null, $secure = false, $httponly = false, $samesite = 'Lax'): bool

Source: `wire/core/Session.php`

Add a SetCookie response header

## Arguments

- `$name` `string`
- `$value` `string|null|false`
- `$expires` (optional) `int`
- `$path` (optional) `string`
- `$domain` (optional) `string|null`
- `$secure` (optional) `bool`
- `$httponly` (optional) `bool`
- `$samesite` (optional) `string` One of 'Strict', 'Lax', 'None'

## Return value

bool

## Since

3.0.178
