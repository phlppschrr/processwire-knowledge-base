# $pages->statusChangeReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page's status is about to be changed and saved

Previous status may be accessed at `$page->statusPrevious`.

## Usage

~~~~~
// basic usage
$result = $pages->statusChangeReady($page);

// usage with all arguments
$result = $pages->statusChangeReady(Page $page);
~~~~~

## Hookable

- Hookable method name: `statusChangeReady`
- Implementation: `___statusChangeReady`
- Hook with: `$pages->statusChangeReady()`

## Arguments

- `$page` `Page`
