# PagesVersions

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Inherits: `Wire`
Implements: `Module`

PagesVersions


Provides a version control API for pages in ProcessWire.
$pagesVersions

~~~~~
// Note: API provided by $pagesVersions API variable
// present with PagesVersions module is installed.

// Get page and add a new version of it
$page = $pages->get(1234);
$page->title = 'New title';
$version = $pagesVersions->addPageVersion($page);
echo $version; // i.e. "2"

// Get version 2 of a page
$pageV2 = $pagesVersions->getPageVersion($page, 2);

// Update a version of a page
$pageV2->title = "Updated title";
$pagesVersions->savePageVersion($pageV2);

// Restore version to live page
$pagesVersions->restorePageVersion($pageV2);

// Delete page version
$pagesVersions->deletePageVersion($pageV2);
~~~~~

## Hookable Methods

- [`allowPageVersions(Page $page): bool`](method-___allowpageversions.md)

@todo test change of template in version

Methods:
- [`getPageVersion(Page $page, int $version, array $options = []): Page|NullPage`](method-getpageversion.md) Get requested page version in a copy of given page
- [`loadPageVersion(Page $page, int|string|PageVersionInfo $version, array $options = []): bool`](method-loadpageversion.md) Load and populate version data to given page
- [`getPageVersions(Page $page, array $options = []): PageVersionInfo[]|Page[]`](method-getpageversions.md) Get all versions for given page
- [`getPageVersionInfo(Page $page, int $version): PageVersionInfo|null`](method-getpageversioninfo.md) Get info for given page and version
- [`getPageVersionInfos(Page $page, array $options = []): PageVersionInfo[]`](method-getpageversioninfos.md) Get just PageVersionInfo objects for all versions of given page
- [`getAllPagesWithVersions(): PageArray`](method-getallpageswithversions.md) Get all pages that have 1 or more versions available
- [`hasPageVersion(Page $page, int|string|PageVersionInfo $version = 0): bool|int`](method-haspageversion.md) Does page have the given version?
- [`hasPageVersions(Page $page): int`](method-haspageversions.md) Return quantity of versions available for given page
- [`addPageVersion(Page $page, array $options = []): int`](method-addpageversion.md) Add a new page version and return the added version number
- [`savePageVersion(Page $page, int|PageVersionInfo $version = 0, array $options = []): int|array`](method-savepageversion.md) Save a page version
- [`deletePageVersion(Page $page, int $version = 0): int`](method-deletepageversion.md) Delete specific page version
- [`deleteAllPageVersions(Page $page): int`](method-deleteallpageversions.md) Delete all versions for given page
- [`deleteAllVersions(bool $areYouSure = false): int`](method-deleteallversions.md) Delete all versions across all pages
- [`restorePageVersion(Page $page, int $version = 0, array $options = []): Page|bool`](method-restorepageversion.md) Restore a page version to be the live version
- [`getSleepValueFromPage(Page $page, Field $field): array|int|string|false`](method-getsleepvaluefrompage.md) Get sleep value from given live page
- [`getSleepValueFromDatabase(Page $page, Field $field): array|int|mixed|string`](method-getsleepvaluefromdatabase.md) Get sleep value from the page field’s field_name table data in database
- [`deletePageFieldVersion(Page $page, Field $field, int $version): bool`](method-deletepagefieldversion.md) Delete a page field version
- [`pageVersionNumber(Page $page, $version = 0): int`](method-pageversionnumber.md) Get the version number of given page or 0 if not versioned
- [`getUnsupportedFields(?Page $page = null): Field[]`](method-getunsupportedfields.md) Get fields where versions are not supported
- [`allowPageVersions(Page $page): bool`](method-___allowpageversions.md) (hookable) Is given page allowed to have versions?
- [`getNextPageVersionNumber(Page $page): int`](method-getnextpageversionnumber.md) Get next available version number for given page
