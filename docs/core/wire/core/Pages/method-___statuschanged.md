# $pages->___statusChanged(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page status has been changed and saved

Previous status may be accessed at `$page->statusPrevious`.

## Usage

~~~~~
// basic usage
$result = $pages->___statusChanged($page);

// usage with all arguments
$result = $pages->___statusChanged(Page $page);
~~~~~

## Arguments

- `$page` `Page`
