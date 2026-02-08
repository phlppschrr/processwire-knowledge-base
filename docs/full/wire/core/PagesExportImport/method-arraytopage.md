# PagesExportImport::arrayToPage()

Source: `wire/core/PagesExportImport.php`

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
