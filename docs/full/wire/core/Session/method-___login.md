# $session->___login($name, $pass, $force = false): User|null

Source: `wire/core/Session.php`

Login a user with the given name and password

Also sets them to the current user.

~~~~~
$u = $session->login('bob', 'laj3939$a');
if($u) {
  echo "Welcome Bob";
} else {
  echo "Sorry Bob";
}
~~~~~

## Arguments

- string|User $name May be user name or User object.
- string $pass Raw, non-hashed password.
- bool $force Specify boolean true to login user without requiring a password ($pass argument can be blank, or anything). You can also use the `$session->forceLogin($user)` method to force a login without a password.

## Return value

User|null Return the $user if the login was successful or null if not.

## Throws

- WireException
