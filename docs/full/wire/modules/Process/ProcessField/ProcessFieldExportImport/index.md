# ProcessFieldExportImport

Source: `wire/modules/Process/ProcessField/ProcessFieldExportImport.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

Handles import/export for ProcessField

Methods:
- [`getExportData(array $exportFields): array`](method-getexportdata.md) Return export data for all given $exportFields
- [`buildExport(): InputfieldForm`](method-___buildexport.md) (hookable) Execute export
- [`buildInputDataForm(): InputfieldForm`](method-___buildinputdataform.md) (hookable) Build Textarea input form to pass JSON data into
- [`buildImport(): InputfieldForm`](method-___buildimport.md) (hookable) Execute import
- [`processImport()`](method-___processimport.md) (hookable) Commit changed field data
