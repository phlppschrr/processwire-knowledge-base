# $page->hasAccessRole($role, $type = 'view'): bool

Source: `wire/core/Page.php`

Returns whether this page has the given access role

Given access role may be a role name, role ID or Role object.

## Arguments

- string|int|Role $role
- string $type May be 'view', 'edit', 'create' or 'add' (default is 'view')

## Return value

bool
