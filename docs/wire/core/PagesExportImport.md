# PagesExportImport

Source: `wire/core/PagesExportImport.php`

ProcessWire Pages Export/Import Helpers

Pages Exporter/Importer
Methods for exporting and importing pages from one installation to another.
$porter
This class is primarily used interactively through the core `ProcessPagesExportImport` module, but
can also be used from its API, described here.
~~~~~
$porter = new PagesExportImport(); // works in any version
$porter = $pages->porter(); // 3.0.253+ only
~~~~~


ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## getExportPath()

Get the path where ZIP exports are stored


@param string $subdir Specify a subdirectory name if you want it to create it.
  If it exists, it will create a numbered version of the subdir to ensure it is unique.

@return string

## cleanupFiles()

Remove files and directories in /site/assets/backups/PagesExportImport/ that are older than $maxAge


@param int $maxAge Maximum age in seconds (default=3600)

@return int Number of files/dirs removed

## exportZIP()

Export given PageArray to a ZIP file


@param PageArray $items

@param array $options

@return string Path+filename to ZIP file

## importZIP()

Import ZIP file to create pages


@param string $filename Path+filename to ZIP file

@param array $options
 - `commit` (bool): Commit/save the changes now? Specify false to perform a test import. (default=true).
 - `update` (bool): Allow update of existing pages? (default=true)
 - `create` (bool): Allow creation of new pages? (default=true)
 - `parent` (Page|string|int): Parent Page, path or ID. Omit to use import data (default=0).
 - `template` (Template|string|int): Template object, name or ID. Omit to use import data (default=0).
 - `fieldNames` (array): Import only these field names, or omit to use all import data (default=[]).
 - `changeStatus` (bool): Allow status to be changed aon existing pages? (default=true)
 - `changeSort` (bool): Allow sort and sortfield to be changed on existing pages? (default=true)
- Note: all the "change" prefix options require update=true.

@return PageArray|bool

## exportJSON()

Export a PageArray to JSON string


@param PageArray $items

@param array $options

@return string JSON string of pages

## importJSON()

Import a PageArray from a JSON string

Given JSON string must be one previously exported by the `exportJSON()` method in this class.


@param string $json JSON string of exported data to import

@param array $options
 - `commit` (bool): Commit/save the changes now? Specify false to perform a test import. (default=true).
 - `update` (bool): Allow update of existing pages? (default=true)
 - `create` (bool): Allow creation of new pages? (default=true)
 - `parent` (Page|string|int): Parent Page, path or ID. Omit to use import data (default=0).
 - `template` (Template|string|int): Template object, name or ID. Omit to use import data (default=0).
 - `fieldNames` (array): Import only these field names, or omit to use all import data (default=[]).
 - `changeStatus` (bool): Allow status to be changed aon existing pages? (default=true)
 - `changeSort` (bool): Allow sort and sortfield to be changed on existing pages? (default=true)
- Note: all the "change" prefix options require update=true.

@return PageArray|bool

## pagesToArray()

Given a PageArray export it to a portable PHP array


@param PageArray $items

@param array $options Additional options to modify behavior
 - `fieldNames` (array): Export oly these field names, when specified. (default=[])

@return array

## pageToArray()

Export Page object to an array


@param Page $page

@param array $options
 - `exportTarget` (string): Export target of 'zip' or 'json' (default=json)

@return array

## arrayToPages()

Import an array of page data to create or update pages

Provided array ($a) must originate from the pagesToArray() method format.


@param array $a Array of import data

@param array $options
 - `count` (bool):  Return count of imported pages, rather than PageArray? Reduces memory requirements. (default=false)
 - `pageArray` (PageArray): PageArray object to populate, or omit to return new PageArray (default=null)

@return PageArray|int

@throws WireException

## arrayToPage()

Import an array of page data to a new Page (or update existing page)

Provided array ($a) must originate from the pageToArray() method format.

Returns a Page on success or a NullPage on failure. Errors, warnings and messages related to the
import can be pulled from `$page->errors()`, `$page->warnings()` and `$page->messages()`.

The following options may be used with the `$options` argument:
 - `commit` (bool): Commit/save the changes now? (default=true). Specify false to perform a test run.
 - `update` (bool): Allow update of existing pages? (default=true)
 - `create` (bool): Allow creation of new pages? (default=true)
 - `parent` (Page|string|int): Parent Page, path or ID. Omit to use import data (default=0).
 - `template` (Template|string|int): Template object, name or ID. Omit to use import data (default=0).
 - `fieldNames` (array): Import only these field names, or omit to use all import data (default=[]).
 - `changeStatus` (bool): Allow status to be changed aon existing pages? (default=true)
 - `changeSort` (bool): Allow sort and sortfield to be changed on existing pages? (default=true)
 - `replaceTemplates` (array): Array of import-data template name to replacement template name (default=[])
 - `replaceFields` (array): Array of import-data field name to replacement field name (default=[])
 - `originalRootUrl` (string): Original root URL (not including hostname)
 - `originalHost` (string): Original hostname

The following options are for future use and not currently applicable:
 - `changeTemplate` (bool): Allow template to be changed on existing pages? (default=false)
 - `changeParent` (bool): Allow parent to be changed on existing pages? (default=false)
 - `changeName` (bool): Allow name to be changed on existing pages? (default=false)
 - `replaceParents` (array): Array of import-data parent path to replacement parent path (default=[])


@param array $a

@param array $options Options to modify default behavior, see method description.

@return Page|NullPage

@throws WireException

## importGetPage()

Get the page to import to

@param array $a Import data

@param array $options Import settings

@param array $errors Errors array

@return NullPage|Page

## importGetTemplate()

Get the Page Template to use for import

@param array $a Import data

@param array $options Import options

@param array $errors Errors array

@return Template|null

## importGetParent()

Get the parent of the page being imported

@param array $a Import data

@param array $options Import options

@param array $errors Errors array

@return Page|NullPage

## importPageSettings()

Import native page settings

@param Page $page

@param array $settings Contents of the import data 'settings' array

@param array $options

## importFieldValue()

Import value for a single field

@param Page $page

@param Field $field

@param array|string|int|float $importValue

@param array $options Looks only at 'commit' option to determine when testing

## importFileFieldValue()

Import a files/images field and populate to given $page

@param Page $page

@param Field $field

@param array $data Export value of file field

@param array $options

## getImportInfo()

Return array of info about the given import data array

This also populates the given import data ($a) with an '_info' property, which is an array containing
all of the import info returned by this method. For each item in the 'pages' index it also populates
an '_importToID' property containing the ID of the existing local page to update, or 0 if it should be
a newly created page.

Return value:
~~~~~
array(
  'numNew' => 0,
  'numExisting' => 0,
  'missingParents' => [ '/path/to/parent/' ],
  'missingTemplates' => [ 'basic-page-hello' ],
  'missingFields' => [ 'some_field', 'another_field' ],
  'missingFieldsTypes' => [ 'some_field' => 'FieldtypeText', 'another_field' => 'FieldtypeTextarea' ]
  'mismatchedFields' => [ 'some_field' => 'FieldtypeText' ] // field name => expected type
  'missingTemplateFields' => [ 'template_name' => [ 'field1', 'field2', etc ] ]
);
~~~~~


@param array $a Import data array

@return array

## getFieldInfo()

Returns array of information about given Field

Populates the following indexes in the returned array:

 - `exportable` (bool): True if field is exportable, false if not.
 - `reason` (string): Reason why field is not exportable (when exportable==false).


@param Field $field

@return array
