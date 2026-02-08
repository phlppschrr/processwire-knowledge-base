# $pages->cloneReady(Page $page, Page $copy)

Source: `wire/core/Pages.php`

Hook called when a page is about to be cloned, but before data has been touched

## Usage

~~~~~
// basic usage
$result = $pages->cloneReady($page, $copy);

// usage with all arguments
$result = $pages->cloneReady(Page $page, Page $copy);
~~~~~

## Hookable

- Hookable method name: `cloneReady`
- Implementation: `___cloneReady`
- Hook with: `$pages->cloneReady()`

## Arguments

- `$page` `Page` The original page to be cloned
- `$copy` `Page` The actual clone about to be saved
