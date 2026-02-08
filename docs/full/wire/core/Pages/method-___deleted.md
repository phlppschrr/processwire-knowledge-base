# $pages->deleted(Page $page, array $options = array())

Source: `wire/core/Pages.php`

Hook called after a page and its data have been deleted

## Usage

~~~~~
// basic usage
$result = $pages->deleted($page);

// usage with all arguments
$result = $pages->deleted(Page $page, array $options = array());
~~~~~

## Hookable

- Hookable method name: `deleted`
- Implementation: `___deleted`
- Hook with: `$pages->deleted()`

## Arguments

- `$page` `Page` Page that was deleted
- `$options` (optional) `array` Options passed to delete method (since 3.0.163)
