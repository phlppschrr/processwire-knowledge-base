# $pagesExportImport->exportJSON(PageArray $items, array $options = array()): string

Source: `wire/core/PagesExportImport.php`

Export a PageArray to JSON string

## Usage

~~~~~
// basic usage
$string = $pagesExportImport->exportJSON($items);

// usage with all arguments
$string = $pagesExportImport->exportJSON(PageArray $items, array $options = array());
~~~~~

## Arguments

- `$items` `PageArray`
- `$options` (optional) `array`

## Return value

- `string` JSON string of pages
