# $pagesVersionsFiles->pageVersion(Page $page, $version): NullPage|Page

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Ensure that given page is given version, and return version page if it isn't already

## Usage

~~~~~
// basic usage
$nullPage = $pagesVersionsFiles->pageVersion($page, $version);

// usage with all arguments
$nullPage = $pagesVersionsFiles->pageVersion(Page $page, $version);
~~~~~

## Arguments

- `$page` `Page`
- `$version` `int` Page version or 0 to get live page

## Return value

- `NullPage|Page`
