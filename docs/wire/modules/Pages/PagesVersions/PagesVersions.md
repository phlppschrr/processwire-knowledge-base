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

## getPageVersion()

*****************************************************************************
PUBLIC API

## getPageVersion()

Get requested page version in a copy of given page

~~~~~
$page = $pages->get(1234);
$pageV2 = $pagesVersions->getPageVersion($page, 2);
~~~~~


@param Page $page Page that version is for

@param int $version Version number to get

@param array $options
 - `names` (array): Optionally load only these field/property names from version.

@return Page|NullPage
 - Returned page is a clone/copy of the given page updated for version data.
 - Returns a `NullPage` if requested version is not found or not allowed.

## loadPageVersion()

Load and populate version data to given page

This is similar to the `getPageVersion()` method except that it populates
the given `$page` rather than populating and returning a cloned copy of it.


@param Page $page

@param int|string|PageVersionInfo $version

@param array $options
 - `names` (array): Optionally load only these field/property names from version.

@return bool True if version data was available and populated, false if not

## getPageVersions()

Get all versions for given page

~~~~~
$page = $pages->get(1234);
$versions = $pagesVersions->getPageVersions($page);
foreach($versions as $p) {
  echo $p->get('_version')->version; // i.e. 2, 3, 4, etc.
}
~~~~~


@param Page $page

@param array $options
 - `getInfo` (bool): Specify true to instead get PageVersionInfo objects (default=false)
 - `sort` (string): Sort by property, one of: 'created', '-created', 'version', '-version' (default='-created')
 - `version` (array): Limit to this version number, for internal use (default=0)

@return PageVersionInfo[]|Page[]
 - Returns Array of `Page` objects or array of `PageVersionInfo` objects if `getInfo` requested.
 - When returning pages, version info is in `$page->_version` value of each page,
   which is a `PageVersionInfo` object.

@throws WireException

## getPageVersionInfo()

Get info for given page and version

~~~~~
// get info for version 2
$info = $pagesVersions->getPageVersionInfo($page, 2);
if($info) {
  echo "Version: $info->version <br />";
  echo "Created: $info->createdStr by {$info->createdUser->name} <br />";
  echo "Description: $info->descriptionHtml";
} else {
  echo "Version does not exist";
}
~~~~~


@param Page $page

@param int $version

@return PageVersionInfo|null

## getPageVersionInfos()

Get just PageVersionInfo objects for all versions of given page

This is the same as using the getPageVersions() method with the `getInfo` option.


~~~~~
$page = $pages->get(1234);
$infos = $pagesVersions->getPageVersionInfos($page);
foreach($infos as $info) {
  echo "<li>$info->version: $descriptionHtml</li>"; // i.e. "2: Hello world"
}
~~~~~


@param Page $page

@param array $options
 - `sort`: Sort by property, one of: 'created', '-created', 'version', '-version' (default='-created')

@return PageVersionInfo[]

## getAllPagesWithVersions()

Get all pages that have 1 or more versions available


@return PageArray

## hasPageVersion()

Does page have the given version?


@param Page $page

@param int|string|PageVersionInfo $version Version number or omit to return quantity of versions

@return bool|int
 - Returns boolean true or false if a non-empty $version argument was specified.
 - Returns integer with quantity of versions of no $version was specified.

## hasPageVersions()

Return quantity of versions available for given page

This is the same as calling the `hasPageVersion()` method
with $version argument omitted.


@param Page $page

@return int

## addPageVersion()

Add a new page version and return the added version number

~~~~~
$page = $pages->get(1234);
$version = $pagesVersions->addPageVersion($page);
echo "Added version $version for page $page";
~~~~~


@param Page $page

@param array $options
 - `description` (string): Optional text description for version.
 - `names` (array): Names of fields/properties to include in the version or omit for all.

@return int Version number or 0 if no version created

@throws WireException|\PDOException

## savePageVersion()

Save a page version


@param Page $page

@param int|PageVersionInfo $version Version number or PageVersionInfo
 - If given version number is greater than 0 and version doesn't exist, it will be added.
 - If 0 or omitted and given page is already a version, its version will be updated.
 - If 0 or omitted and given page is not a version, this method behaves the same as
   the `addPageVersion()` method and returns the added version number.

@param array $options
 - `description` (string): Optional text description for version (default='')
 - `update` (bool): Update version if it already exists (default=true)

@return int|array Returns version number saved or added or 0 on fail

@throws WireException|\PDOException

## deletePageVersion()

Delete specific page version

~~~~~~
// delete version 2 of the page
$page = $pages->get(1234);
$pagesVersions->deletePageVersion($page, 2);

// this does the same thing as above
$pageV2 = $pagesVersions->getPageVersion($page, 2);
$pagesVersions->deletePageVersion($pageV2);
~~~~~~


@param Page $page Page to delete version from, or page having the version you want to delete.

@param int $version Version number to delete or omit if given $page is the version you want to delete.

@return int Number of DB rows deleted as part of the deletion process

## deleteAllPageVersions()

Delete all versions for given page


@param Page $page

@return int Number of versions deleted

## deleteAllVersions()

Delete all versions across all pages


@param bool $areYouSure Specify true to indicate you are sure you want to do this

@return int Quantity of versions deleted

## restorePageVersion()

Restore a page version to be the live version

Note that the restored page is saved to the database, replacing the current live version.
So consider whether you should backup the live version (by using addPageVersion) before
restoring a version to it.

~~~~~
// restore version 2 to live page
$page = $pages->get(1234);
$pagesVersions->restore($page, 2); // restore version 2

// this does the same as the above
$pageV2 = $pagesVersions->getPageVersion($page, 2);
$pagesVersions->restore($pageV2);
~~~~~


@param Page $page Page to restore version to or a page that was loaded as a version.

@param int $version Version number to restore. Can be omitted if given $page is already a version.

@param array $options
 - `names` (array): Names of fields/properties to restore or omit for all (default=[])
 - `useTempVersion` (bool): Create a temporary version and restore from that? (default=auto-detect).
    This is necessary for some Fieldtypes like nested repeaters. Use of it is auto-detected so
    it is not necessary to specify this when using the public API.

@return Page|bool Returns restored version page on success or false on fail

@throws WireException

## getPageFieldVersion()

************************************************************************
INTERNAL API

## getSleepValueFromPage()

Get sleep value from given live page

@param Page $page

@param Field $field

@return array|int|string|false

## getSleepValueFromDatabase()

Get sleep value from the page field’s field_name table data in database

@todo method currently not used but may be later

@param Page $page

@param Field $field

@return array|int|mixed|string

## deletePageFieldVersion()

Delete a page field version

This should not be called independently of deletePageVersion() as this
method does not delete any files connected to the version.

@param Page $page

@param Field $field

@param int $version

@return bool

## pageVersionNumber()

Get the version number of given page or 0 if not versioned


@param Page $page

@param int|string|PageVersionInfo Optional version argument to use, if omitted it pulls from $page
 - If this argument resolves to a number, that number is returned.
 - If this argument is omitted, the version number is pulled from the $page argument.

@return int

## getUnsupportedFields()

Get fields where versions are not supported


@param Page|null $page Page to limit check to or omit for all fields

@return Field[] Returned array of Field objects is indexed by Field name

## ___allowPageVersions()

Is given page allowed to have versions?


@param Page $page

@return bool

## getNextPageVersionNumber()

Get next available version number for given page


@param Page $page

@return int

## hookBeforePagesSave()

*****************************************************************************
HOOKS
