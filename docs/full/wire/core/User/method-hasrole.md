# User::hasRole()

Source: `wire/core/User.php`

Does this user have the given Role?


~~~~~
if($user->hasRole('editor')) {
  // user has the editor role
}
~~~~~

@param string|Role|int $role May be Role name, object or ID.

@return bool
