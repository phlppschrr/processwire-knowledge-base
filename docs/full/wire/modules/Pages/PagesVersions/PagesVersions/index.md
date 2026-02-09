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

Methods:
- [`getPageVersion(Page $page, $version, array $options = [])`](method-getpageversion.md)
- [`getPageVersion(Page $page, int $version, array $options = []): Page|NullPage`](method-getpageversion.md)
- [`loadPageVersion(Page $page, int|string|PageVersionInfo $version, array $options = []): bool`](method-loadpageversion.md)
- [`getPageVersions(Page $page, array $options = []): PageVersionInfo[]|Page[]`](method-getpageversions.md)
- [`getPageVersionInfo(Page $page, int $version): PageVersionInfo|null`](method-getpageversioninfo.md)
- [`getPageVersionInfos(Page $page, array $options = []): PageVersionInfo[]`](method-getpageversioninfos.md)
- [`getAllPagesWithVersions(): PageArray`](method-getallpageswithversions.md)
- [`hasPageVersion(Page $page, int|string|PageVersionInfo $version = 0): bool|int`](method-haspageversion.md)
- [`hasPageVersions(Page $page): int`](method-haspageversions.md)
- [`addPageVersion(Page $page, array $options = []): int`](method-addpageversion.md)
- [`savePageVersion(Page $page, int|PageVersionInfo $version = 0, array $options = []): int|array`](method-savepageversion.md)
- [`deletePageVersion(Page $page, int $version = 0): int`](method-deletepageversion.md)
- [`deleteAllPageVersions(Page $page): int`](method-deleteallpageversions.md)
- [`deleteAllVersions(bool $areYouSure = false): int`](method-deleteallversions.md)
- [`restorePageVersion(Page $page, int $version = 0, array $options = []): Page|bool`](method-restorepageversion.md)
- [`getPageFieldVersion(Page $page, Field $field, $version, array $options = [])`](method-getpagefieldversion.md)
- [`getSleepValueFromPage(Page $page, Field $field): array|int|string|false`](method-getsleepvaluefrompage.md)
- [`getSleepValueFromDatabase(Page $page, Field $field): array|int|mixed|string`](method-getsleepvaluefromdatabase.md)
- [`deletePageFieldVersion(Page $page, Field $field, int $version): bool`](method-deletepagefieldversion.md)
- [`pageVersionNumber(Page $page, $version = 0): int`](method-pageversionnumber.md)
- [`getUnsupportedFields(?Page $page = null): Field[]`](method-getunsupportedfields.md)
- [`allowPageVersions(Page $page): bool`](method-___allowpageversions.md) (hookable)
- [`getNextPageVersionNumber(Page $page): int`](method-getnextpageversionnumber.md)
- [`hookBeforePagesSave(HookEvent $event)`](method-hookbeforepagessave.md)

HOOKABLE METHODS
----------------

- [`allowPageVersions(Page $page): bool`](method-___allowpageversions.md)

@todo test change of template in version
