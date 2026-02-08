# Page::hasAccessRole()

Source: `wire/core/Page.php`

Returns whether this page has the given access role

Given access role may be a role name, role ID or Role object.


@param string|int|Role $role

@param string $type May be 'view', 'edit', 'create' or 'add' (default is 'view')

@return bool
