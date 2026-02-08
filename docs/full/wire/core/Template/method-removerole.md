# $template->removeRole($role, $type = 'view'): $this

Source: `wire/core/Template.php`

Remove a Role to this template for view, edit, create, or add permission

## Arguments

- Role|int|string $role Role instance, id or name
- string $type Type of role being added, one of: view, edit, create, add. (default=view) You may also specify “all” to remove the role entirely from all possible usages in the template.

## Return value

$this

## Throws

- WireException If given $role cannot be resolved
