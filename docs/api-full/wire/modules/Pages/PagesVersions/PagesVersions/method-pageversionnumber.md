# $pagesVersions->pageVersionNumber(Page $page, $version = 0): int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get the version number of given page or 0 if not versioned

## Usage

~~~~~
// basic usage
$int = $pagesVersions->pageVersionNumber($page);

// usage with all arguments
$int = $pagesVersions->pageVersionNumber(Page $page, $version = 0);
~~~~~

## Arguments

- `$page` `Page`
- int|string|PageVersionInfo Optional version argument to use, if omitted it pulls from $page - If this argument resolves to a number, that number is returned. - If this argument is omitted, the version number is pulled from the $page argument.

## Return value

- `int`
