# $pagesVersions->restorePageVersion(Page $page, $version = 0, array $options = []): Page|bool

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Restore a page version to be the live version

Note that the restored page is saved to the database, replacing the current live version.
So consider whether you should backup the live version (by using addPageVersion) before
restoring a version to it.

## Example

~~~~~
// restore version 2 to live page
$page = $pages->get(1234);
$pagesVersions->restore($page, 2); // restore version 2

// this does the same as the above
$pageV2 = $pagesVersions->getPageVersion($page, 2);
$pagesVersions->restore($pageV2);
~~~~~

## Usage

~~~~~
// basic usage
$page = $pagesVersions->restorePageVersion($page);

// usage with all arguments
$page = $pagesVersions->restorePageVersion(Page $page, $version = 0, array $options = []);
~~~~~

## Arguments

- `$page` `Page` Page to restore version to or a page that was loaded as a version.
- `$version` (optional) `int` Version number to restore. Can be omitted if given $page is already a version.
- `$options` (optional) `array` - `names` (array): Names of fields/properties to restore or omit for all (default=[]) - `useTempVersion` (bool): Create a temporary version and restore from that? (default=auto-detect). This is necessary for some Fieldtypes like nested repeaters. Use of it is auto-detected so it is not necessary to specify this when using the public API.

## Return value

- `Page|bool` Returns restored version page on success or false on fail

## Exceptions

- `WireException`
