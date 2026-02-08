# $selectableOptionManager->findOptionsByProperty(Field $field, $property, $operator, $value): SelectableOptionArray

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Perform a partial match on title of options

## Arguments

- Field $field
- string $property Either 'title' or 'value'. May also be blank (to imply 'either') if operator is '=' or '!='
- string $operator
- string $value Value to find

## Return value

SelectableOptionArray
