# $pagesExportImport->pagesToArray(PageArray $items, array $options = array()): array

Source: `wire/core/PagesExportImport.php`

Given a PageArray export it to a portable PHP array

## Usage

~~~~~
// basic usage
$array = $pagesExportImport->pagesToArray($items);

// usage with all arguments
$array = $pagesExportImport->pagesToArray(PageArray $items, array $options = array());
~~~~~

## Arguments

- `$items` `PageArray`
- `$options` (optional) `array` Additional options to modify behavior - `fieldNames` (array): Export oly these field names, when specified. (default=[])

## Return value

- `array`
