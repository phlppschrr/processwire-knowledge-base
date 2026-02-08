# $pages->___restoreReady(Page $page)

Source: `wire/core/Pages.php`

Hook called when a page is about to be moved OUT of the trash (restored)

## Usage

~~~~~
// basic usage
$result = $pages->___restoreReady($page);

// usage with all arguments
$result = $pages->___restoreReady(Page $page);
~~~~~

## Arguments

- `$page` `Page` Page that is about to be restored

## Since

3.0.235
