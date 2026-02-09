# $pagesExportImport->exportZIP(PageArray $items, array $options = array()): string

Source: `wire/core/PagesExportImport.php`

Export given PageArray to a ZIP file

## Usage

~~~~~
// basic usage
$string = $pagesExportImport->exportZIP($items);

// usage with all arguments
$string = $pagesExportImport->exportZIP(PageArray $items, array $options = array());
~~~~~

## Arguments

- `$items` `PageArray`
- `$options` (optional) `array`

## Return value

- `string` Path+filename to ZIP file
