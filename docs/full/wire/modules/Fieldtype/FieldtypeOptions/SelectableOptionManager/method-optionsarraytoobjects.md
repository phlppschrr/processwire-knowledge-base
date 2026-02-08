# $selectableOptionManager->optionsArrayToObjects(array $value): SelectableOptionArray

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Convert an array of option arrays, to a SelectableOptionArray of SelectableOption objects

## Usage

~~~~~
// basic usage
$selectableOptionArray = $selectableOptionManager->optionsArrayToObjects($value);

// usage with all arguments
$selectableOptionArray = $selectableOptionManager->optionsArrayToObjects(array $value);
~~~~~

## Arguments

- `$value` `array`

## Return value

- `SelectableOptionArray`

## Exceptions

- `WireException`
