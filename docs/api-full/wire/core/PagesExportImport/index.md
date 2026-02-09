# PagesExportImport

Source: `wire/core/PagesExportImport.php`

Inherits: `Wire`

## Summary

ProcessWire Pages Export/Import Helpers

Common methods:
- [`getExportPath()`](method-getexportpath.md)
- [`cleanupFiles()`](method-cleanupfiles.md)
- [`exportZIP()`](method-exportzip.md)
- [`importZIP()`](method-importzip.md)
- [`exportJSON()`](method-exportjson.md)

Pages Exporter/Importer
Methods for exporting and importing pages from one installation to another.
`$porter`
This class is primarily used interactively through the core `ProcessPagesExportImport` module, but
can also be used from its API, described here.
~~~~~
$porter = new PagesExportImport(); // works in any version
$porter = $pages->porter(); // 3.0.253+ only
~~~~~

## Methods
- [`getExportPath(string $subdir = ''): string`](method-getexportpath.md) Get the path where ZIP exports are stored
- [`cleanupFiles(int $maxAge = 3600): int`](method-cleanupfiles.md) Remove files and directories in /site/assets/backups/PagesExportImport/ that are older than $maxAge
- [`exportZIP(PageArray $items, array $options = array()): string`](method-exportzip.md) Export given PageArray to a ZIP file
- [`importZIP(string $filename, array $options = array()): PageArray|bool`](method-importzip.md) Import ZIP file to create pages
- [`exportJSON(PageArray $items, array $options = array()): string`](method-exportjson.md) Export a PageArray to JSON string
- [`importJSON(string $json, array $options = array()): PageArray|bool`](method-importjson.md) Import a PageArray from a JSON string
- [`pagesToArray(PageArray $items, array $options = array()): array`](method-pagestoarray.md) Given a PageArray export it to a portable PHP array
- [`pageToArray(Page $page, array $options): array`](method-pagetoarray.md) Export Page object to an array
- [`arrayToPages(array $a, array $options = array()): PageArray|int`](method-arraytopages.md) Import an array of page data to create or update pages
- [`arrayToPage(array $a, array $options = array()): Page|NullPage`](method-arraytopage.md) Import an array of page data to a new Page (or update existing page)
- [`importGetPage(array &$a, array &$options, array &$errors): NullPage|Page`](method-importgetpage.md) Get the page to import to
- [`importGetTemplate(array &$a, array &$options, array &$errors): Template|null`](method-importgettemplate.md) Get the Page Template to use for import
- [`importGetParent(array &$a, array &$options, array &$errors): Page|NullPage`](method-importgetparent.md) Get the parent of the page being imported
- [`importPageSettings(Page $page, array $settings, array $options)`](method-importpagesettings.md) Import native page settings
- [`importFieldValue(Page $page, Field $field, array|string|int|float $importValue, array $options)`](method-importfieldvalue.md) Import value for a single field
- [`importFileFieldValue(Page $page, Field $field, array $data, array $options = array())`](method-importfilefieldvalue.md) Import a files/images field and populate to given $page
- [`getImportInfo(array &$a): array`](method-getimportinfo.md) Return array of info about the given import data array
- [`getFieldInfo(Field $field): array`](method-getfieldinfo.md) Returns array of information about given Field
