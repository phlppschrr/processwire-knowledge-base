# Role::addPermission()

Source: `wire/core/Role.php`

Add the given Permission string, id or object.

This is the same as `$role->permissions->add($permission)` except this one will accept ID or name.

@param string|int|Permission $permission Permission object, name or id.

@return bool Returns false if permission not recognized, true otherwise
