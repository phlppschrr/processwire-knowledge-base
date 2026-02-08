# $fieldtype->___getSelectorInfo(Field $field, array $data = array()): array

Source: `wire/core/Fieldtype.php`

Return array with information about what properties and operators can be used with this field.

## Usage

~~~~~
// basic usage
$array = $fieldtype->___getSelectorInfo($field);

// usage with all arguments
$array = $fieldtype->___getSelectorInfo(Field $field, array $data = array());
~~~~~

## Arguments

- `$field` `Field`
- `$data` (optional) `array` Array of extra data, when/if needed

## Return value

- `array` See `FieldSelectorInfo` class for details.
