# $pagesExportImport->pageToArray(Page $page, array $options): array

Source: `wire/core/PagesExportImport.php`

Export Page object to an array

## Usage

~~~~~
// basic usage
$array = $pagesExportImport->pageToArray($page, $options);

// usage with all arguments
$array = $pagesExportImport->pageToArray(Page $page, array $options);
~~~~~

## Arguments

- `$page` `Page`
- `$options` `array` - `exportTarget` (string): Export target of 'zip' or 'json' (default=json)

## Return value

- `array`
