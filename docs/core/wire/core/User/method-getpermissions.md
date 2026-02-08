# $user->getPermissions(?Page $page = null): PageArray

Source: `wire/core/User.php`

Get this user’s permissions, optionally within the context of a Page.

~~~~~
// Get all permissions the user has across their roles
$permissions = $user->getPermissions();

// Get all permissions the user has for $page
$permissions = $user->getPermissions($page);
~~~~~

## Arguments

- Page|null $page Optional page to check against

## Return value

PageArray of Permission objects
