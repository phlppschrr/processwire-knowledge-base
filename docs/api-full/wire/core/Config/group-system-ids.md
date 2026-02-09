# Config: system-IDs

Source: `wire/core/Config.php`

- `$rootPageID: int` Page ID of homepage (usually 1)
- `$adminRootPageID: int` Page ID of admin root page
- `$trashPageID: int` Page ID of the trash page.
- `$loginPageID: int` Page ID of the admin login page.
- `$http404PageID: int` Page ID of the 404 “page not found” page.
- `$usersPageID: int` Page ID of the page having users as children.
- `$usersPageIDs: array` Populated if multiple possible users page IDs (parent for users pages)
- `$rolesPageID: int` Page ID of the page having roles as children.
- `$permissionsPageID: int` Page ID of the page having permissions as children.
- `$guestUserPageID: int` Page ID of the guest (default/not-logged-in) user.
- `$superUserPageID: int` Page ID of the original superuser (created during installation).
- `$guestUserRolePageID: int` Page ID of the guest user role (inherited by all users, not just guest).
- `$superUserRolePageID: int` Page ID of the superuser role.
- `$userTemplateID: int` Template ID of the user template.
- `$userTemplateIDs: array` Array of template IDs when multiple allowed for users.
- `$roleTemplateID: int` Template ID of the role template.
- `$permissionTemplateID: int` Template ID of the permission template.
- `$externalPageID: int` Page ID of page assigned to `$page` API variable when externally bootstrapped
- `$preloadPageIDs: array` Page IDs of pages that will always be preloaded at beginning of request
