# PagesExportImport

Source: `wire/core/PagesExportImport.php`

Inherits: `Wire`

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

Methods:
- [`getExportPath(string $subdir = ''): string`](method-getexportpath.md)
- [`cleanupFiles(int $maxAge = 3600): int`](method-cleanupfiles.md)
- [`exportZIP(PageArray $items, array $options = array()): string`](method-exportzip.md)
- [`importZIP(string $filename, array $options = array()): PageArray|bool`](method-importzip.md)
- [`exportJSON(PageArray $items, array $options = array()): string`](method-exportjson.md)
- [`importJSON(string $json, array $options = array()): PageArray|bool`](method-importjson.md)
- [`pagesToArray(PageArray $items, array $options = array()): array`](method-pagestoarray.md)
- [`pageToArray(Page $page, array $options): array`](method-pagetoarray.md)
- [`arrayToPages(array $a, array $options = array()): PageArray|int`](method-arraytopages.md)
- [`arrayToPage(array $a, array $options = array()): Page|NullPage`](method-arraytopage.md)
- [`importGetPage(array &$a, array &$options, array &$errors): NullPage|Page`](method-importgetpage.md)
- [`importGetTemplate(array &$a, array &$options, array &$errors): Template|null`](method-importgettemplate.md)
- [`importGetParent(array &$a, array &$options, array &$errors): Page|NullPage`](method-importgetparent.md)
- [`importPageSettings(Page $page, array $settings, array $options)`](method-importpagesettings.md)
- [`importFieldValue(Page $page, Field $field, array|string|int|float $importValue, array $options)`](method-importfieldvalue.md)
- [`importFileFieldValue(Page $page, Field $field, array $data, array $options = array())`](method-importfilefieldvalue.md)
- [`getImportInfo(array &$a): array`](method-getimportinfo.md)
- [`getFieldInfo(Field $field): array`](method-getfieldinfo.md)
