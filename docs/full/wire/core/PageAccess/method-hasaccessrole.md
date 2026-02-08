# $pageAccess->hasAccessRole(Page $page, $role, $type = 'view'): bool

Source: `wire/core/PageAccess.php`

Returns whether this page has the given access role

Given access role may be a role name, role ID or Role object

## Arguments

- Page $page
- string|int|Role $role
- string $type Default is 'view', but you may specify 'create' or 'add' as well

## Return value

bool
