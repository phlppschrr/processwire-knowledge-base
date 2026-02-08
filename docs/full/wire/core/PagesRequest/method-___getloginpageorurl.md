# PagesRequest::___getLoginPageOrUrl()

Source: `wire/core/PagesRequest.php`

Get login Page object or URL to redirect to for login needed to access given $page

- When a Page is returned, it is suggested the Page be rendered in this request.
- When a string/URL is returned, it is suggested you redirect to it.
- When null is returned no login page or URL could be identified and 404 should render.

@param Page|null $page Page that access was requested to or omit to get admin login page

@return string|Page|null Login page object or string w/redirect URL, null if 404
