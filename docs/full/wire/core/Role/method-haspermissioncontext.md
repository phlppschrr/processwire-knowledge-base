# $role->hasPermissionContext($has, Permission $permission, Wire $context): bool

Source: `wire/core/Role.php`

Return whether the role has the permission within the context of a Page or Template

## Arguments

- `$has` `bool` Result from the hasPermission() method
- `$permission` `Permission` Permission to check
- `$context` `Wire` Must be a Template or Page

## Return value

bool
