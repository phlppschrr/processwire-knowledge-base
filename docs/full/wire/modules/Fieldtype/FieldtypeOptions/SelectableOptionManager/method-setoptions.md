# $selectableOptionManager->setOptions(Field $field, $options, $allowDelete = true): array

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Set current options for $field, identify and acting on added, deleted, updated options

## Arguments

- Field $field
- array|SelectableOptionArray $options Array of SelectableOption objects For new options specify 0 for the 'id' property.
- bool $allowDelete Allow options to be deleted? If false, the options marked for deletion can be retrieved via $this->getRemovedOptions($field);

## Return value

array containing ('added' => cnt, 'updated' => cnt, 'deleted' => cnt, 'marked' => cnt) note: 'marked' means marked for deletion

## Throws

- WireException
