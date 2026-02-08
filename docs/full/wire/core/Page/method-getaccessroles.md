# $page->getAccessRoles($type = 'view'): PageArray

Source: `wire/core/Page.php`

Return Roles (PageArray) that have access to this page

This is determined from the page's template. If the page's template has roles turned off,
then it will go down the tree till it finds usable roles to use and inherit from.

## Arguments

- `$type` (optional) `string` May be 'view', 'edit', 'create' or 'add' (default='view')

## Return value

PageArray of Role objects
