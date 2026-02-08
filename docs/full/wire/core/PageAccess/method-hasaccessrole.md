# PageAccess::hasAccessRole()

Source: `wire/core/PageAccess.php`

Returns whether this page has the given access role

Given access role may be a role name, role ID or Role object

@param Page $page

@param string|int|Role $role

@param string $type Default is 'view', but you may specify 'create' or 'add' as well

@return bool
