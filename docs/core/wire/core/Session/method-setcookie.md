# $session->setCookie($name, $value, $expires = 0, $path = '/', $domain = null, $secure = false, $httponly = false, $samesite = 'Lax'): bool

Source: `wire/core/Session.php`

Add a SetCookie response header

## Arguments

- string $name
- string|null|false $value
- int $expires
- string $path
- string|null $domain
- bool $secure
- bool $httponly
- string $samesite One of 'Strict', 'Lax', 'None'

## Return value

bool

## Meta

- @since 3.0.178
