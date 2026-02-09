# $selectableOptionManager->getOptionsByID(Field $field, array $ids): SelectableOptionArray|SelectableOption[]

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Shortcut to get options by ID number

## Usage

~~~~~
// basic usage
$selectableOptionArray = $selectableOptionManager->getOptionsByID($field, $ids);

// usage with all arguments
$selectableOptionArray = $selectableOptionManager->getOptionsByID(Field $field, array $ids);
~~~~~

## Arguments

- `$field` `Field`
- `$ids` `array`

## Return value

- `SelectableOptionArray|SelectableOption[]`
