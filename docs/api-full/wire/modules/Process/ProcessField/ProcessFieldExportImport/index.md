# ProcessFieldExportImport

Source: `wire/modules/Process/ProcessField/ProcessFieldExportImport.php`

Inherits: `Wire`

## Summary

Handles import/export for ProcessField

Common methods:
- [`getExportData()`](method-getexportdata.md)
- [`buildExport()`](method-___buildexport.md)
- [`buildInputDataForm()`](method-___buildinputdataform.md)
- [`buildImport()`](method-___buildimport.md)
- [`processImport()`](method-___processimport.md)

Groups:
Group: [other](group-other.md)

## Methods
- [`getExportData(array $exportFields): array`](method-getexportdata.md) Return export data for all given $exportFields
- [`buildExport(): InputfieldForm`](method-___buildexport.md) (hookable) Execute export
- [`buildInputDataForm(): InputfieldForm`](method-___buildinputdataform.md) (hookable) Build Textarea input form to pass JSON data into
- [`buildImport(): InputfieldForm`](method-___buildimport.md) (hookable) Execute import
- [`processImport()`](method-___processimport.md) (hookable) Commit changed field data
