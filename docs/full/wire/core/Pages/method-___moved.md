# $pages->moved(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page has been moved from one parent to another

Note the previous parent is accessible in the `$page->parentPrevious` property.

## Usage

~~~~~
// basic usage
$result = $pages->moved($page);

// usage with all arguments
$result = $pages->moved(Page $page);
~~~~~

## Hookable

- Hookable method name: `moved`
- Implementation: `___moved`
- Hook with: `$pages->moved()`

## Arguments

- `$page` `Page` Page that was moved.
