# $fieldgroups->___setImportData(Fieldgroup $fieldgroup, array $data): array

Source: `wire/core/Fieldgroups.php`

Given an export data array, import it back to the class and return what happened

Changes are not committed until the item is saved

## Arguments

- Fieldgroup $fieldgroup
- array $data

## Return value

array Returns array( [property_name] => array( 'old' => 'old value',	// old value, always a string 'new' => 'new value',	// new value, always a string 'error' => 'error message or blank if no error' )

## Throws

- WireException if given invalid data
