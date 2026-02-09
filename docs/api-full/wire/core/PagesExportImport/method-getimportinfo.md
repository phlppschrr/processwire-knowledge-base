# $pagesExportImport->getImportInfo(array &$a): array

Source: `wire/core/PagesExportImport.php`

Return array of info about the given import data array

This also populates the given import data ($a) with an '_info' property, which is an array containing
all of the import info returned by this method. For each item in the 'pages' index it also populates
an '_importToID' property containing the ID of the existing local page to update, or 0 if it should be
a newly created page.

Return value:

## Example

~~~~~
array(
  'numNew' => 0,
  'numExisting' => 0,
  'missingParents' => [ '/path/to/parent/' ],
  'missingTemplates' => [ 'basic-page-hello' ],
  'missingFields' => [ 'some_field', 'another_field' ],
  'missingFieldsTypes' => [ 'some_field' => 'FieldtypeText', 'another_field' => 'FieldtypeTextarea' ]
  'mismatchedFields' => [ 'some_field' => 'FieldtypeText' ] // field name => expected type
  'missingTemplateFields' => [ 'template_name' => [ 'field1', 'field2', etc ] ]
);
~~~~~

## Usage

~~~~~
// basic usage
$array = $pagesExportImport->getImportInfo($a);

// usage with all arguments
$array = $pagesExportImport->getImportInfo(array &$a);
~~~~~

## Arguments

- `$a` `array` Import data array

## Return value

- `array`
