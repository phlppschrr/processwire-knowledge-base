# $selectableOptionManager->updateOptions(Field $field, $options): int

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Update options for field

## Usage

~~~~~
// basic usage
$int = $selectableOptionManager->updateOptions($field, $options);

// usage with all arguments
$int = $selectableOptionManager->updateOptions(Field $field, $options);
~~~~~

## Arguments

- `$field` `Field`
- `$options` `array|SelectableOptionArray`

## Return value

- `int` Number of options updated
