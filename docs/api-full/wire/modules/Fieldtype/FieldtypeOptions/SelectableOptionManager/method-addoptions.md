# $selectableOptionManager->addOptions(Field $field, $options): int

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Add the given option titles for $field

## Usage

~~~~~
// basic usage
$int = $selectableOptionManager->addOptions($field, $options);

// usage with all arguments
$int = $selectableOptionManager->addOptions(Field $field, $options);
~~~~~

## Arguments

- `$field` `Field`
- `$options` `array|SelectableOptionArray`

## Return value

- `int` Number of options added
