# $session->forceLogin($user): User|null

Source: `wire/core/Session.php`

Login a user without requiring a password

## Example

~~~~~
// login bob without knowing his password
$u = $session->forceLogin('bob');
~~~~~

## Usage

~~~~~
// basic usage
$user = $session->forceLogin($user);
~~~~~

## Arguments

- `$user` `string|User` Username or User object

## Return value

- `User|null` Returns User object on success, or null on failure
