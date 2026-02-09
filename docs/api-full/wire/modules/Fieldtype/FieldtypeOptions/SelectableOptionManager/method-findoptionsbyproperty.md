# $selectableOptionManager->findOptionsByProperty(Field $field, $property, $operator, $value): SelectableOptionArray

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Perform a partial match on title of options

## Usage

~~~~~
// basic usage
$selectableOptionArray = $selectableOptionManager->findOptionsByProperty($field, $property, $operator, $value);

// usage with all arguments
$selectableOptionArray = $selectableOptionManager->findOptionsByProperty(Field $field, $property, $operator, $value);
~~~~~

## Arguments

- `$field` `Field`
- `$property` `string` Either 'title' or 'value'. May also be blank (to imply 'either') if operator is '=' or '!='
- `$operator` `string`
- `$value` `string` Value to find

## Return value

- `SelectableOptionArray`
