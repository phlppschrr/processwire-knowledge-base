# $pagesType->deleteReady(Page $page)

Source: `wire/core/PagesType.php`

Hook called when a page is about to be deleted, but before data has been touched

## Usage

~~~~~
// basic usage
$result = $pagesType->deleteReady($page);

// usage with all arguments
$result = $pagesType->deleteReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `deleteReady`
- Implementation: `___deleteReady`
- Hook with: `$pagesType->deleteReady()`

## Arguments

- `$page` `Page`

## Since

3.0.128
