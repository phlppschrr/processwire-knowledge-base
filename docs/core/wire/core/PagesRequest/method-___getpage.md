# $pagesRequest->getPage(array $options = array()): Page|NullPage

Source: `wire/core/PagesRequest.php`

Get the requested page

- Populates identified urlSegments or page numbers to $input.
- Returns NullPage for error, call getResponseCode() and/or getResponseMessage() for details.
- Returned page should be validated with getPageForUser() method before rendering it.
- Call getFile() method afterwards to see if request resolved to file managed by returned page.

## Usage

~~~~~
// basic usage
$page = $pagesRequest->getPage();

// usage with all arguments
$page = $pagesRequest->getPage(array $options = array());
~~~~~

## Hookable

- Hookable method name: `getPage`
- Implementation: `___getPage`
- Hook with: `$pagesRequest->getPage()`

## Arguments

- `$options` (optional) `array`

## Return value

- `Page|NullPage`
