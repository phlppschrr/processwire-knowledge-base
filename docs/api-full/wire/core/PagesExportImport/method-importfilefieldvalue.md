# $pagesExportImport->importFileFieldValue(Page $page, Field $field, array $data, array $options = array())

Source: `wire/core/PagesExportImport.php`

Import a files/images field and populate to given $page

## Usage

~~~~~
// basic usage
$result = $pagesExportImport->importFileFieldValue($page, $field, $data);

// usage with all arguments
$result = $pagesExportImport->importFileFieldValue(Page $page, Field $field, array $data, array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$data` `array` Export value of file field
- `$options` (optional) `array`
