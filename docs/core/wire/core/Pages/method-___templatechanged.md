# $pages->___templateChanged(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page's template has been changed

Note the previous template is available in the `$page->templatePrevious` property.

## Usage

~~~~~
// basic usage
$result = $pages->___templateChanged($page);

// usage with all arguments
$result = $pages->___templateChanged(Page $page);
~~~~~

## Arguments

- `$page` `Page` Page that had its template changed.
