# $user->getPermissions(?Page $page = null): PageArray

Source: `wire/core/User.php`

Get this user’s permissions, optionally within the context of a Page.

## Example

~~~~~
// Get all permissions the user has across their roles
$permissions = $user->getPermissions();

// Get all permissions the user has for $page
$permissions = $user->getPermissions($page);
~~~~~

## Usage

~~~~~
// basic usage
$items = $user->getPermissions();

// usage with all arguments
$items = $user->getPermissions(?Page $page = null);
~~~~~

## Arguments

- `$page` (optional) `Page|null` Optional page to check against

## Return value

- `PageArray` of Permission objects
