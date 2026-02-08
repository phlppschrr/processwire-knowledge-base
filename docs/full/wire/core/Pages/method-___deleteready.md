# $pages->deleteReady(Page $page, array $options = array())

Source: `wire/core/Pages.php`

Hook called when a page is about to be deleted, but before data has been touched

This is different from a before `Pages::delete` hook because this hook is called once it has
been confirmed that the page is deleteable and *will* be deleted.

## Usage

~~~~~
// basic usage
$result = $pages->deleteReady($page);

// usage with all arguments
$result = $pages->deleteReady(Page $page, array $options = array());
~~~~~

## Hookable

- Hookable method name: `deleteReady`
- Implementation: `___deleteReady`
- Hook with: `$pages->deleteReady()`

## Arguments

- `$page` `Page` Page that is about to be deleted.
- `$options` (optional) `array` Options passed to delete method (since 3.0.163)
