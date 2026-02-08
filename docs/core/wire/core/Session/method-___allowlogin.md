# $session->___allowLogin($name, $user = null): bool

Source: `wire/core/Session.php`

Allow the user $name to login? Provided for use by hooks.

## Arguments

- string $name User login name
- User|null $user User object

## Return value

bool True if allowed to login, false if not (hooks may modify this)
