# $pagesRequest->___getLoginPageOrUrl(?Page $page = null): string|Page|null

Source: `wire/core/PagesRequest.php`

Get login Page object or URL to redirect to for login needed to access given $page

- When a Page is returned, it is suggested the Page be rendered in this request.
- When a string/URL is returned, it is suggested you redirect to it.
- When null is returned no login page or URL could be identified and 404 should render.

## Usage

~~~~~
// basic usage
$string = $pagesRequest->___getLoginPageOrUrl();

// usage with all arguments
$string = $pagesRequest->___getLoginPageOrUrl(?Page $page = null);
~~~~~

## Arguments

- `$page` (optional) `Page|null` Page that access was requested to or omit to get admin login page

## Return value

- `string|Page|null` Login page object or string w/redirect URL, null if 404
