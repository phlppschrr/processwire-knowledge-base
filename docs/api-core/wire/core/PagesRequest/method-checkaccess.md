# $pagesRequest->checkAccess(Page $page, User $user): Page|string|null

Source: `wire/core/PagesRequest.php`

Check that the current user has access to the page and return it

If the user doesn’t have access, then a login Page or NULL (for 404) is returned instead.

## Usage

~~~~~
// basic usage
$page = $pagesRequest->checkAccess($page, $user);

// usage with all arguments
$page = $pagesRequest->checkAccess(Page $page, User $user);
~~~~~

## Arguments

- `$page` `Page`
- `$user` `User`

## Return value

- `Page|string|null` Page to render, URL to redirect to, or null for 404
