# PagesRequest::___getPage()

Source: `wire/core/PagesRequest.php`

Get the requested page

- Populates identified urlSegments or page numbers to $input.
- Returns NullPage for error, call getResponseCode() and/or getResponseMessage() for details.
- Returned page should be validated with getPageForUser() method before rendering it.
- Call getFile() method afterwards to see if request resolved to file managed by returned page.

@param array $options

@return Page|NullPage
