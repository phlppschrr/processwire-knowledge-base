# Template: access

Source: `wire/core/Template.php`

- `$useRoles: int|bool` Whether or not this template defines access.
- `$roles: PageArray` Roles assigned to this template for view access.
- `$editRoles: array` Array of Role IDs that may edit pages using this template.
- `$addRoles: array` Array of Role IDs that may add pages using this template.
- `$createRoles: array` Array of Role IDs that may create pages using this template.
- `$rolesPermissions: array` Override permissions: Array indexed by role ID with values as permission ID (add) or negative permission ID (revoke).
- `$noInherit: int` Disable role inheritance? Specify 1 to prevent edit/create/add access from inheriting to children, or 0 for default inherit behavior.
- `$redirectLogin: int` Redirect when no access: 0 = 404, 1 = login page, url = URL to redirect to, `int(>1)` = ID of page to redirect to.
- `$guestSearchable: int` Pages appear in search results even when user doesnt have access? (0=no, 1=yes)
