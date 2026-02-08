# $fieldtypeMulti->getSelectorInfo(Field $field, array $data = array()): array

Source: `wire/core/FieldtypeMulti.php`

Return array with information about what properties and operators can be used with this field

## Usage

~~~~~
// basic usage
$array = $fieldtypeMulti->getSelectorInfo($field);

// usage with all arguments
$array = $fieldtypeMulti->getSelectorInfo(Field $field, array $data = array());
~~~~~

## Hookable

- Hookable method name: `getSelectorInfo`
- Implementation: `___getSelectorInfo`
- Hook with: `$fieldtypeMulti->getSelectorInfo()`

## Arguments

- `$field` `Field`
- `$data` (optional) `array` Array of extra data, when/if needed

## Return value

- `array`
