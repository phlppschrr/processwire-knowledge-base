# $session->login($name, $pass, $force = false): User|null

Source: `wire/core/Session.php`

Login a user with the given name and password

Also sets them to the current user.

## Example

~~~~~
$u = $session->login('bob', 'laj3939$a');
if($u) {
  echo "Welcome Bob";
} else {
  echo "Sorry Bob";
}
~~~~~

## Usage

~~~~~
// basic usage
$user = $session->login($name, $pass);

// usage with all arguments
$user = $session->login($name, $pass, $force = false);
~~~~~

## Hookable

- Hookable method name: `login`
- Implementation: `___login`
- Hook with: `$session->login()`

## Arguments

- `$name` `string|User` May be user name or User object.
- `$pass` `string` Raw, non-hashed password.
- `$force` (optional) `bool` Specify boolean true to login user without requiring a password ($pass argument can be blank, or anything). You can also use the `$session->forceLogin($user)` method to force a login without a password.

## Return value

- `User|null` Return the $user if the login was successful or null if not.

## Exceptions

- `WireException`
