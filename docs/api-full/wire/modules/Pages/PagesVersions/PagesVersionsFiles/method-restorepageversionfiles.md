# $pagesVersionsFiles->restorePageVersionFiles(Page $page, $version): int

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Restore files from version into live $page

## Usage

~~~~~
// basic usage
$int = $pagesVersionsFiles->restorePageVersionFiles($page, $version);

// usage with all arguments
$int = $pagesVersionsFiles->restorePageVersionFiles(Page $page, $version);
~~~~~

## Arguments

- `$page` `Page`
- `$version` `int`

## Return value

- `int`
