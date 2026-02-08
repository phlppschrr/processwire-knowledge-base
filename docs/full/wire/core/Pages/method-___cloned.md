# $pages->cloned(Page $page, Page $copy)

Source: `wire/core/Pages.php`

Hook called when a page has been cloned

## Usage

~~~~~
// basic usage
$result = $pages->cloned($page, $copy);

// usage with all arguments
$result = $pages->cloned(Page $page, Page $copy);
~~~~~

## Hookable

- Hookable method name: `cloned`
- Implementation: `___cloned`
- Hook with: `$pages->cloned()`

## Arguments

- `$page` `Page` The original page to be cloned
- `$copy` `Page` The completed cloned version of the page
