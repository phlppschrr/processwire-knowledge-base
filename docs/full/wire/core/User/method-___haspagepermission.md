# User::___hasPagePermission()

Source: `wire/core/User.php`

Does this user have named permission for the given Page?

This is a basic permission check and it is recommended that you use those from the PagePermissions module instead.
You use the PagePermissions module by calling the editable(), addable(), etc., functions on a page object.
The PagePermissions does use this function for some of it's checking.


@param string|Permission

@param Page|null $page Optional page to check against

@return bool
