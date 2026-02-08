# Config: system-IDs

Source: `wire/core/Config.php`

@property int $rootPageID Page ID of homepage (usually 1)

@property int $adminRootPageID Page ID of admin root page

@property int $trashPageID Page ID of the trash page.

@property int $loginPageID Page ID of the admin login page.

@property int $http404PageID Page ID of the 404 “page not found” page.

@property int $usersPageID Page ID of the page having users as children.

@property array $usersPageIDs Populated if multiple possible users page IDs (parent for users pages)

@property int $rolesPageID Page ID of the page having roles as children.

@property int $permissionsPageID Page ID of the page having permissions as children.

@property int $guestUserPageID Page ID of the guest (default/not-logged-in) user.

@property int $superUserPageID Page ID of the original superuser (created during installation).

@property int $guestUserRolePageID Page ID of the guest user role (inherited by all users, not just guest).

@property int $superUserRolePageID Page ID of the superuser role.

@property int $userTemplateID Template ID of the user template.

@property array $userTemplateIDs Array of template IDs when multiple allowed for users.

@property int $roleTemplateID Template ID of the role template.

@property int $permissionTemplateID Template ID of the permission template.

@property int $externalPageID Page ID of page assigned to $page API variable when externally bootstrapped

@property array $preloadPageIDs Page IDs of pages that will always be preloaded at beginning of request
