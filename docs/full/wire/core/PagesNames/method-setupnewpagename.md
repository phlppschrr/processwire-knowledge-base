# $pagesNames->setupNewPageName(Page $page, $format = ''): string

Source: `wire/core/PagesNames.php`

Assign a name to given Page (if it doesn’t already have one)

## Usage

~~~~~
// basic usage
$string = $pagesNames->setupNewPageName($page);

// usage with all arguments
$string = $pagesNames->setupNewPageName(Page $page, $format = '');
~~~~~

## Arguments

- `$page` `Page` Page to setup a new name for
- `$format` (optional) `string` Optional format string to use for name

## Return value

- `string` Returns page name that was assigned
