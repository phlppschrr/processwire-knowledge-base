# $fieldgroups->getExportData(Fieldgroup $fieldgroup): array

Source: `wire/core/Fieldgroups.php`

Export config data for the given fieldgroup

## Usage

~~~~~
// basic usage
$array = $fieldgroups->getExportData($fieldgroup);

// usage with all arguments
$array = $fieldgroups->getExportData(Fieldgroup $fieldgroup);
~~~~~

## Hookable

- Hookable method name: `getExportData`
- Implementation: `___getExportData`
- Hook with: `$fieldgroups->getExportData()`

## Arguments

- `$fieldgroup` `Fieldgroup`

## Return value

- `array`
