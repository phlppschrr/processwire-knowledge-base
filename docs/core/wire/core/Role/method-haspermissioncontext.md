# Role::hasPermissionContext()

Source: `wire/core/Role.php`

Return whether the role has the permission within the context of a Page or Template

@param bool $has Result from the hasPermission() method

@param Permission $permission Permission to check

@param Wire $context Must be a Template or Page

@return bool
