# $template->removeRole($role, $type = 'view'): $this

Source: `wire/core/Template.php`

Remove a Role to this template for view, edit, create, or add permission

## Arguments

- `$role` `Role|int|string` Role instance, id or name
- `$type` (optional) `string` Type of role being added, one of: view, edit, create, add. (default=view) You may also specify “all” to remove the role entirely from all possible usages in the template.

## Return value

$this

## Throws

- WireException If given $role cannot be resolved
