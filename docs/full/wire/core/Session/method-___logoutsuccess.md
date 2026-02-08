# $session->logoutSuccess(User $user)

Source: `wire/core/Session.php`

Logout success method for hooks

## Usage

~~~~~
// basic usage
$result = $session->logoutSuccess($user);

// usage with all arguments
$result = $session->logoutSuccess(User $user);
~~~~~

## Hookable

- Hookable method name: `logoutSuccess`
- Implementation: `___logoutSuccess`
- Hook with: `$session->logoutSuccess()`

## Arguments

- `$user` `User` User that logged in
