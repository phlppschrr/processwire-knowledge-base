# $selectableOptionManager->deleteOptions(Field $field, $options): int

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Delete the given options for $field

## Usage

~~~~~
// basic usage
$int = $selectableOptionManager->deleteOptions($field, $options);

// usage with all arguments
$int = $selectableOptionManager->deleteOptions(Field $field, $options);
~~~~~

## Arguments

- `$field` `Field`
- `$options` `array|SelectableOptionArray`

## Return value

- `int` Number of options deleted
