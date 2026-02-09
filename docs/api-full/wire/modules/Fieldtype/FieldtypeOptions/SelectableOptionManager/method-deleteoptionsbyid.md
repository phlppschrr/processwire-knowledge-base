# $selectableOptionManager->deleteOptionsByID(Field $field, array $ids): int

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Delete the given option IDs

## Usage

~~~~~
// basic usage
$int = $selectableOptionManager->deleteOptionsByID($field, $ids);

// usage with all arguments
$int = $selectableOptionManager->deleteOptionsByID(Field $field, array $ids);
~~~~~

## Arguments

- `$field` `Field`
- `$ids` `array`

## Return value

- `int` Number of options deleted
