# $pagesVersionsFiles->copyPageVersionFiles(Page $page, $version): bool|int

Source: `wire/modules/Pages/PagesVersions/PagesVersionsFiles.php`

Copy files for given $page into version directory

## Usage

~~~~~
// basic usage
$bool = $pagesVersionsFiles->copyPageVersionFiles($page, $version);

// usage with all arguments
$bool = $pagesVersionsFiles->copyPageVersionFiles(Page $page, $version);
~~~~~

## Arguments

- `$page` `Page`
- `$version` `int`

## Return value

- `bool|int`
