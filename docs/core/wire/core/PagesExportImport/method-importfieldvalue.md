# $pagesExportImport->importFieldValue(Page $page, Field $field, $importValue, array $options)

Source: `wire/core/PagesExportImport.php`

Import value for a single field

## Usage

~~~~~
// basic usage
$result = $pagesExportImport->importFieldValue($page, $field, $importValue, $options);

// usage with all arguments
$result = $pagesExportImport->importFieldValue(Page $page, Field $field, $importValue, array $options);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$importValue` `array|string|int|float`
- `$options` `array` Looks only at 'commit' option to determine when testing
