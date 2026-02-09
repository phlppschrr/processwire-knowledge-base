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
Method: [getExportPath()](method-getexportpath.md)
Method: [cleanupFiles()](method-cleanupfiles.md)
Method: [exportZIP()](method-exportzip.md)
Method: [importZIP()](method-importzip.md)
Method: [exportJSON()](method-exportjson.md)
Method: [importJSON()](method-importjson.md)
Method: [pagesToArray()](method-pagestoarray.md)
Method: [pageToArray()](method-pagetoarray.md)
Method: [arrayToPages()](method-arraytopages.md)
Method: [arrayToPage()](method-arraytopage.md)
Method: [importGetPage()](method-importgetpage.md)
Method: [importGetTemplate()](method-importgettemplate.md)
Method: [importGetParent()](method-importgetparent.md)
Method: [importPageSettings()](method-importpagesettings.md)
Method: [importFieldValue()](method-importfieldvalue.md)
Method: [importFileFieldValue()](method-importfilefieldvalue.md)
Method: [getImportInfo()](method-getimportinfo.md)
Method: [getFieldInfo()](method-getfieldinfo.md)
