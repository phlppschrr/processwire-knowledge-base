# $tfa->___start($name, $pass): bool

Source: `wire/core/Tfa.php`

Start 2-factor authentication

On successful authentication of user, this method performs a redirect to the next step.
If user does not exist, they are not allowed to login, or fails to authenticate, this method
returns a boolean false. If user does not have 2FA enabled, or is remembered from a previous
TFA login, then this method returns true, but user still needs to be authenticated.

If preferred, you can ignore the return value, as this method will perform redirects whenever
it needs to move on to the next 2FA step.

## Arguments

- `$name` `string`
- `$pass` `string`

## Return value

bool
