# $template->addPermissionByRole($permission, $role, $test = false): bool

Source: `wire/core/Template.php`

Add a permission that applies to users having a specific role with pages using this template

Note that the change is not committed until you save() the template.

## Arguments

- Permission|int|string $permission Permission object, name, or id
- Role|int|string $role Role object, name or id
- bool $test Specify true to only test if an update would be made, without changing anything

## Return value

bool Returns true if an update was made (or would be made), false if not
