# $pages->restored(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page has been moved OUT of the trash (restored)

## Usage

~~~~~
// basic usage
$result = $pages->restored($page);

// usage with all arguments
$result = $pages->restored(Page $page);
~~~~~

## Hookable

- Hookable method name: `restored`
- Implementation: `___restored`
- Hook with: `$pages->restored()`

## Arguments

- `$page` `Page` Page that was restored
