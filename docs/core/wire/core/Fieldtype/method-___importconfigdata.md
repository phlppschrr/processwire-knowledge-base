# $fieldtype->___importConfigData(Field $field, array $data): array

Source: `wire/core/Fieldtype.php`

Convert an array of exported data to a format that will be understood internally

This is the opposite of the exportConfigData() method.
Most modules can use the default implementation provided here.

## Arguments

- Field $field
- array $data

## Return value

array Data as given and modified as needed. Also included is $data[errors], an associative array indexed by property name containing errors that occurred during import of config data.
