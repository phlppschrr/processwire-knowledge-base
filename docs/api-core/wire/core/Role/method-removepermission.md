# $role->removePermission($permission): bool

Source: `wire/core/Role.php`

Remove the given permission string, id or object.

This is the same as `$role->permissions->remove($permission)` except this one will accept ID or name.

## Usage

~~~~~
// basic usage
$bool = $role->removePermission($permission);
~~~~~

## Arguments

- `$permission` `string|int|Permission` Permission object, name or id.

## Return value

- `bool` false if permission not recognized, true otherwise
