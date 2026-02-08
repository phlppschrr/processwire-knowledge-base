# Role::removePermission()

Source: `wire/core/Role.php`

Remove the given permission string, id or object.

This is the same as `$role->permissions->remove($permission)` except this one will accept ID or name.

@param string|int|Permission $permission Permission object, name or id.

@return bool false if permission not recognized, true otherwise
