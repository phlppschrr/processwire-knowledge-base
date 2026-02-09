# $pagesExportImport->importGetPage(array &$a, array &$options, array &$errors): NullPage|Page

Source: `wire/core/PagesExportImport.php`

Get the page to import to

## Usage

~~~~~
// basic usage
$nullPage = $pagesExportImport->importGetPage($a, $options, $errors);

// usage with all arguments
$nullPage = $pagesExportImport->importGetPage(array &$a, array &$options, array &$errors);
~~~~~

## Arguments

- `$a` `array` Import data
- `$options` `array` Import settings
- `$errors` `array` Errors array

## Return value

- `NullPage|Page`
