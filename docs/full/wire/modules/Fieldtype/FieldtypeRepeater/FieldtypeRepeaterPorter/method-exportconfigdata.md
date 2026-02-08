# $fieldtypeRepeaterPorter->exportConfigData(Field $field, array $data): array

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterPorter.php`

Export configuration values for external consumption

Use this method to externalize any config values when necessary.
For example, internal IDs should be converted to GUIDs where possible.
Most Fieldtype modules can use the default implementation already provided here.

## Usage

~~~~~
// basic usage
$array = $fieldtypeRepeaterPorter->exportConfigData($field, $data);

// usage with all arguments
$array = $fieldtypeRepeaterPorter->exportConfigData(Field $field, array $data);
~~~~~

## Arguments

- `$field` `Field`
- `$data` `array`

## Return value

- `array`
