# Session::forceLogin()

Source: `wire/core/Session.php`

Login a user without requiring a password

~~~~~
// login bob without knowing his password
$u = $session->forceLogin('bob');
~~~~~


@param string|User $user Username or User object

@return User|null Returns User object on success, or null on failure
