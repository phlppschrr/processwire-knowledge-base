# $session->forceLogin($user): User|null

Source: `wire/core/Session.php`

Login a user without requiring a password

~~~~~
// login bob without knowing his password
$u = $session->forceLogin('bob');
~~~~~

## Arguments

- `$user` `string|User` Username or User object

## Return value

User|null Returns User object on success, or null on failure
