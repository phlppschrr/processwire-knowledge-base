# $pages->trashed(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page has been moved to the trash

## Usage

~~~~~
// basic usage
$result = $pages->trashed($page);

// usage with all arguments
$result = $pages->trashed(Page $page);
~~~~~

## Hookable

- Hookable method name: `trashed`
- Implementation: `___trashed`
- Hook with: `$pages->trashed()`

## Arguments

- `$page` `Page` Page that was moved to the trash
