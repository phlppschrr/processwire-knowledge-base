# Role::hasPermission()

Source: `wire/core/Role.php`

Does this role have the given permission name, id or object?

@param string|int|Permission $permission Permission object, name, or id.

@param Page|Template|null $context Optional Page or Template context.

@return bool

@see User::hasPermission()
