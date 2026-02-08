# $template->addRole($role, $type = 'view'): $this

Source: `wire/core/Template.php`

Add a Role to this template for view, edit, create, or add permission

## Arguments

- `$role` `Role|int|string` Role instance, id or name
- `$type` (optional) `string` Type of role being added, one of: view, edit, create, add. (default=view)

## Return value

$this

## Throws

- WireException If given $role cannot be resolved
