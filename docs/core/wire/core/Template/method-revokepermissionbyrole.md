# $template->revokePermissionByRole($permission, $role, $test = false): bool

Source: `wire/core/Template.php`

Revoke a permission that applies to users having a specific role with pages using this template

Note that the change is not committed until you save() the template.

## Arguments

- `$permission` `Permission|int|string` Permission object, name, or id
- `$role` `Role|int|string` Role object, name or id
- `$test` (optional) `bool` Specify true to only test if an update would be made, without changing anything

## Return value

bool Returns true if an update was made (or would be made), false if not
