# $selectableOptionManager->getOptions(Field $field, array $filters = array()): SelectableOptionArray|SelectableOption[]

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Return array of current options for $field

Returned array is indexed by "id$option_id" associative, which is used
as a way to identify existing options vs. new options

## Arguments

- Field $field
- array $filters Any of array(property => array) where property is 'id', 'title' or 'value'.

## Return value

SelectableOptionArray|SelectableOption[]

## Throws

- WireException
