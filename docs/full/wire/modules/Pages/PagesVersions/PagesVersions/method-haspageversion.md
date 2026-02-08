# $pagesVersions->hasPageVersion(Page $page, $version = 0): bool|int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Does page have the given version?

## Arguments

- Page $page
- int|string|PageVersionInfo $version Version number or omit to return quantity of versions

## Return value

bool|int - Returns boolean true or false if a non-empty $version argument was specified. - Returns integer with quantity of versions of no $version was specified.
