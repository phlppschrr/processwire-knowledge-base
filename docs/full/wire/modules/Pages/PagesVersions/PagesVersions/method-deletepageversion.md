# $pagesVersions->deletePageVersion(Page $page, $version = 0): int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Delete specific page version

~~~~~~
// delete version 2 of the page
$page = $pages->get(1234);
$pagesVersions->deletePageVersion($page, 2);

// this does the same thing as above
$pageV2 = $pagesVersions->getPageVersion($page, 2);
$pagesVersions->deletePageVersion($pageV2);
~~~~~~

## Arguments

- Page $page Page to delete version from, or page having the version you want to delete.
- int $version Version number to delete or omit if given $page is the version you want to delete.

## Return value

int Number of DB rows deleted as part of the deletion process
