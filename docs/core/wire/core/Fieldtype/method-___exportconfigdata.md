# $fieldtype->exportConfigData(Field $field, array $data): array

Source: `wire/core/Fieldtype.php`

Export configuration values for external consumption

Use this method to externalize any config values when necessary.
For example, internal IDs should be converted to GUIDs where possible.
Most Fieldtype modules can use the default implementation already provided here.

## Usage

~~~~~
// basic usage
$array = $fieldtype->exportConfigData($field, $data);

// usage with all arguments
$array = $fieldtype->exportConfigData(Field $field, array $data);
~~~~~

## Hookable

- Hookable method name: `exportConfigData`
- Implementation: `___exportConfigData`
- Hook with: `$fieldtype->exportConfigData()`

## Arguments

- `$field` `Field`
- `$data` `array`

## Return value

- `array`
