# $session->___allowLogin($name, $user = null): bool

Source: `wire/core/Session.php`

Allow the user $name to login? Provided for use by hooks.

## Usage

~~~~~
// basic usage
$bool = $session->___allowLogin($name);

// usage with all arguments
$bool = $session->___allowLogin($name, $user = null);
~~~~~

## Arguments

- `$name` `string` User login name
- `$user` (optional) `User|null` User object

## Return value

- `bool` True if allowed to login, false if not (hooks may modify this)
