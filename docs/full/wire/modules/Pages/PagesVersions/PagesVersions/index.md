# PagesVersions

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

PagesVersions

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

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

HOOKABLE METHODS
----------------

@method bool allowPageVersions(Page $page)

@todo test change of template in version

Methods:
Method: [getPageVersion()](method-getpageversion.md)
Method: [getPageVersion()](method-getpageversion.md)
Method: [loadPageVersion()](method-loadpageversion.md)
Method: [getPageVersions()](method-getpageversions.md)
Method: [getPageVersionInfo()](method-getpageversioninfo.md)
Method: [getPageVersionInfos()](method-getpageversioninfos.md)
Method: [getAllPagesWithVersions()](method-getallpageswithversions.md)
Method: [hasPageVersion()](method-haspageversion.md)
Method: [hasPageVersions()](method-haspageversions.md)
Method: [addPageVersion()](method-addpageversion.md)
Method: [savePageVersion()](method-savepageversion.md)
Method: [deletePageVersion()](method-deletepageversion.md)
Method: [deleteAllPageVersions()](method-deleteallpageversions.md)
Method: [deleteAllVersions()](method-deleteallversions.md)
Method: [restorePageVersion()](method-restorepageversion.md)
Method: [getPageFieldVersion()](method-getpagefieldversion.md)
Method: [getSleepValueFromPage()](method-getsleepvaluefrompage.md)
Method: [getSleepValueFromDatabase()](method-getsleepvaluefromdatabase.md)
Method: [deletePageFieldVersion()](method-deletepagefieldversion.md)
Method: [pageVersionNumber()](method-pageversionnumber.md)
Method: [getUnsupportedFields()](method-getunsupportedfields.md)
Method: [___allowPageVersions()](method-___allowpageversions.md)
Method: [getNextPageVersionNumber()](method-getnextpageversionnumber.md)
Method: [hookBeforePagesSave()](method-hookbeforepagessave.md)
