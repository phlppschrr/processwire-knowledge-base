# $role->hasPermissionContext($has, Permission $permission, Wire $context): bool

Source: `wire/core/Role.php`

Return whether the role has the permission within the context of a Page or Template

## Arguments

- bool $has Result from the hasPermission() method
- Permission $permission Permission to check
- Wire $context Must be a Template or Page

## Return value

bool
