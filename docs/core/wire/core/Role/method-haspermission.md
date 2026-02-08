# $role->hasPermission($permission, $context = null): bool

Source: `wire/core/Role.php`

Does this role have the given permission name, id or object?

## Arguments

- `$permission` `string|int|Permission` Permission object, name, or id.
- `$context` (optional) `Page|Template|null` Optional Page or Template context.

## Return value

bool

## See also

- [User::hasPermission()](../User/method-haspermission.md)
