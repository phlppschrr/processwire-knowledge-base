# Page::getAccessRoles()

Source: `wire/core/Page.php`

Return Roles (PageArray) that have access to this page

This is determined from the page's template. If the page's template has roles turned off,
then it will go down the tree till it finds usable roles to use and inherit from.


@param string $type May be 'view', 'edit', 'create' or 'add' (default='view')

@return PageArray of Role objects
