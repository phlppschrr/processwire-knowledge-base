# Exportable

Source: `wire/core/Interfaces.php`

## Summary

For classes that may have their data exported to an array

Common methods:
- [`getExportData()`](method-getexportdata.md)
- [`setImportData()`](method-setimportdata.md)

Classes implementing this interface are also assumed to be able to accept the same

## Methods
- [`getExportData(): array`](method-getexportdata.md) Return export data (may be the same as getTableData from Saveable interface)
- [`setImportData(array $data): array`](method-setimportdata.md) Given an export data array, import it back to the class and return what happened
