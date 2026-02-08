# $role->addPermission($permission): bool

Source: `wire/core/Role.php`

Add the given Permission string, id or object.

This is the same as `$role->permissions->add($permission)` except this one will accept ID or name.

## Arguments

- string|int|Permission $permission Permission object, name or id.

## Return value

bool Returns false if permission not recognized, true otherwise
