# $selectableOptionManager->findOptionsByProperty(Field $field, $property, $operator, $value): SelectableOptionArray

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Perform a partial match on title of options

## Arguments

- `$field` `Field`
- `$property` `string` Either 'title' or 'value'. May also be blank (to imply 'either') if operator is '=' or '!='
- `$operator` `string`
- `$value` `string` Value to find

## Return value

SelectableOptionArray
