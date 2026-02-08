# User::addRole()

Source: `wire/core/User.php`

Add Role to this user

This is the same as `$user->roles->add($role)` except this one will also accept ID or name.

~~~~~
// Add the "editor" role to the $user
$user->addRole('editor');
$user->save();
~~~~~


@param string|int|Role $role May be Role name, object, or ID.

@return bool Returns false if role not recognized, true otherwise
