# Session::___allowLogin()

Source: `wire/core/Session.php`

Allow the user $name to login? Provided for use by hooks.


@param string $name User login name

@param User|null $user User object

@return bool True if allowed to login, false if not (hooks may modify this)
