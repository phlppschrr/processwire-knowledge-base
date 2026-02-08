# $pagesRequest->getRequestPage(): NullPage|Page

Source: `wire/core/PagesRequest.php`

Get page that was requested

If this is different from the Page returned by getPageForUser() then it would
represent the page that the user lacked access to.

## Return value

NullPage|Page
