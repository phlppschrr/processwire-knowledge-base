# $pagesExportImport->importGetParent(array &$a, array &$options, array &$errors): Page|NullPage

Source: `wire/core/PagesExportImport.php`

Get the parent of the page being imported

## Usage

~~~~~
// basic usage
$page = $pagesExportImport->importGetParent($a, $options, $errors);

// usage with all arguments
$page = $pagesExportImport->importGetParent(array &$a, array &$options, array &$errors);
~~~~~

## Arguments

- `$a` `array` Import data
- `$options` `array` Import options
- `$errors` `array` Errors array

## Return value

- `Page|NullPage`
