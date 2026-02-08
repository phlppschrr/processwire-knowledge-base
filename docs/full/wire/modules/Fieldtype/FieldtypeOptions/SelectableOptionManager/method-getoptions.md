# $selectableOptionManager->getOptions(Field $field, array $filters = array()): SelectableOptionArray|SelectableOption[]

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Return array of current options for $field

Returned array is indexed by "id$option_id" associative, which is used
as a way to identify existing options vs. new options

## Usage

~~~~~
// basic usage
$selectableOptionArray = $selectableOptionManager->getOptions($field);

// usage with all arguments
$selectableOptionArray = $selectableOptionManager->getOptions(Field $field, array $filters = array());
~~~~~

## Arguments

- `$field` `Field`
- `$filters` (optional) `array` Any of array(property => array) where property is 'id', 'title' or 'value'.

## Return value

- `SelectableOptionArray|SelectableOption[]`

## Exceptions

- `WireException`
