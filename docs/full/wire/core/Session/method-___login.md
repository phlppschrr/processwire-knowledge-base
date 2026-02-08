# Session::___login()

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


@param string|User $name May be user name or User object.

@param string $pass Raw, non-hashed password.

@param bool $force Specify boolean true to login user without requiring a password ($pass argument can be blank, or anything).
	You can also use the `$session->forceLogin($user)` method to force a login without a password.

@return User|null Return the $user if the login was successful or null if not.

@throws WireException
