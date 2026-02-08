# PageAccess::getAccessParent()

Source: `wire/core/PageAccess.php`

Returns the parent page that has the template from which we get our role/access settings from

@param Page $page

@param string $type Type, one of 'view', 'edit', 'create' or 'add' (default='view')

@param int $level Recursion level for internal use only

@return Page|NullPage Returns NullPage if none found
