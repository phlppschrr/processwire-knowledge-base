# $pagesExportImport->getExportPath($subdir = ''): string

Source: `wire/core/PagesExportImport.php`

Get the path where ZIP exports are stored

## Usage

~~~~~
// basic usage
$string = $pagesExportImport->getExportPath();

// usage with all arguments
$string = $pagesExportImport->getExportPath($subdir = '');
~~~~~

## Arguments

- `$subdir` (optional) `string` Specify a subdirectory name if you want it to create it. If it exists, it will create a numbered version of the subdir to ensure it is unique.

## Return value

- `string`
