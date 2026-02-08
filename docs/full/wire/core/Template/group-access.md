# Template: access

Source: `wire/core/Template.php`

@property int|bool $useRoles Whether or not this template defines access.

@property PageArray $roles Roles assigned to this template for view access.

@property array $editRoles Array of Role IDs that may edit pages using this template.

@property array $addRoles Array of Role IDs that may add pages using this template.

@property array $createRoles Array of Role IDs that may create pages using this template.

@property array $rolesPermissions Override permissions: Array indexed by role ID with values as permission ID (add) or negative permission ID (revoke).

@property int $noInherit Disable role inheritance? Specify 1 to prevent edit/create/add access from inheriting to children, or 0 for default inherit behavior.

@property int $redirectLogin Redirect when no access: 0 = 404, 1 = login page, url = URL to redirect to, int(>1) = ID of page to redirect to.

@property int $guestSearchable Pages appear in search results even when user doesnt have access? (0=no, 1=yes)
