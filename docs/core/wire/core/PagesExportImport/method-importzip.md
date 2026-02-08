# PagesExportImport::importZIP()

Source: `wire/core/PagesExportImport.php`

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
