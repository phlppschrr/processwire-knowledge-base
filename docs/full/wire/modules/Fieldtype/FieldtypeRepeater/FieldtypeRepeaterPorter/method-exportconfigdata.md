# $fieldtypeRepeaterPorter->exportConfigData(Field $field, array $data): array

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterPorter.php`

Export configuration values for external consumption

Use this method to externalize any config values when necessary.
For example, internal IDs should be converted to GUIDs where possible.
Most Fieldtype modules can use the default implementation already provided here.

## Arguments

- Field $field
- array $data

## Return value

array
