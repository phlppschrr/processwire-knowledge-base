# PageAccess::getAccessRoles()

Source: `wire/core/PageAccess.php`

Return the PageArray of roles that have access to this page

This is determined from the page's template. If the page's template has roles turned off,
then it will go down the tree till it finds usable roles to use.

@param Page $page

@param string $type Default is 'view', but you may specify 'edit', 'create' or 'add' to retrieve that type

@return PageArray
