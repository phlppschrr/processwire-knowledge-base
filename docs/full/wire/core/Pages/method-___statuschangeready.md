# $pages->___statusChangeReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page's status is about to be changed and saved

Previous status may be accessed at `$page->statusPrevious`.

## Usage

~~~~~
// basic usage
$result = $pages->___statusChangeReady($page);

// usage with all arguments
$result = $pages->___statusChangeReady(Page $page);
~~~~~

## Arguments

- `$page` `Page`
