# $pagesExportImport->getFieldInfo(Field $field): array

Source: `wire/core/PagesExportImport.php`

Returns array of information about given Field

Populates the following indexes in the returned array:

 - `exportable` (bool): True if field is exportable, false if not.
 - `reason` (string): Reason why field is not exportable (when exportable==false).

## Usage

~~~~~
// basic usage
$array = $pagesExportImport->getFieldInfo($field);

// usage with all arguments
$array = $pagesExportImport->getFieldInfo(Field $field);
~~~~~

## Arguments

- `$field` `Field`

## Return value

- `array`
