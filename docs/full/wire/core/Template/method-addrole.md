# Template::addRole()

Source: `wire/core/Template.php`

Add a Role to this template for view, edit, create, or add permission

@param Role|int|string $role Role instance, id or name

@param string $type Type of role being added, one of: view, edit, create, add. (default=view)

@return $this

@throws WireException If given $role cannot be resolved
