# User::getPermissions()

Source: `wire/core/User.php`

Get this user’s permissions, optionally within the context of a Page.

~~~~~
// Get all permissions the user has across their roles
$permissions = $user->getPermissions();

// Get all permissions the user has for $page
$permissions = $user->getPermissions($page);
~~~~~


@param Page|null $page Optional page to check against

@return PageArray of Permission objects
