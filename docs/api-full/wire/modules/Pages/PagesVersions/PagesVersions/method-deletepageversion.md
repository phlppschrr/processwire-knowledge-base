# $pagesVersions->deletePageVersion(Page $page, $version = 0): int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Delete specific page version

## Example

~~~~~~
// delete version 2 of the page
$page = $pages->get(1234);
$pagesVersions->deletePageVersion($page, 2);

// this does the same thing as above
$pageV2 = $pagesVersions->getPageVersion($page, 2);
$pagesVersions->deletePageVersion($pageV2);
~~~~~~

## Usage

~~~~~
// basic usage
$int = $pagesVersions->deletePageVersion($page);

// usage with all arguments
$int = $pagesVersions->deletePageVersion(Page $page, $version = 0);
~~~~~

## Arguments

- `$page` `Page` Page to delete version from, or page having the version you want to delete.
- `$version` (optional) `int` Version number to delete or omit if given $page is the version you want to delete.

## Return value

- `int` Number of DB rows deleted as part of the deletion process
