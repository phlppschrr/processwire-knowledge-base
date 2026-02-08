# PagesRequest::checkAccess()

Source: `wire/core/PagesRequest.php`

Check that the current user has access to the page and return it

If the user doesn’t have access, then a login Page or NULL (for 404) is returned instead.

@param Page $page

@param User $user

@return Page|string|null Page to render, URL to redirect to, or null for 404
