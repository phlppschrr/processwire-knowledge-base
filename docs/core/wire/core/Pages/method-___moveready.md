# $pages->moveReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page is about to be moved to another parent

Note the previous parent is accessible in the `$page->parentPrevious` property.

## Usage

~~~~~
// basic usage
$result = $pages->moveReady($page);

// usage with all arguments
$result = $pages->moveReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `moveReady`
- Implementation: `___moveReady`
- Hook with: `$pages->moveReady()`

## Arguments

- `$page` `Page` Page that is about to be moved.

## Since

3.0.235
