# $user->removeRole($role): bool

Source: `wire/core/User.php`

Remove Role from this user

This is the same as `$user->roles->remove($role)` except this one will accept ID or name.

~~~~~
// Remove the "editor" role from the $user
$user->removeRole('editor');
$user->save();
~~~~~

## Arguments

- string|int|Role $role May be Role name, object or ID.

## Return value

bool false if role not recognized, true otherwise
