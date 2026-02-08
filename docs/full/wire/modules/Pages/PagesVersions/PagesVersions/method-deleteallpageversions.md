# $pagesVersions->deleteAllPageVersions(Page $page): int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Delete all versions for given page

## Usage

~~~~~
// basic usage
$int = $pagesVersions->deleteAllPageVersions($page);

// usage with all arguments
$int = $pagesVersions->deleteAllPageVersions(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `int` Number of versions deleted
