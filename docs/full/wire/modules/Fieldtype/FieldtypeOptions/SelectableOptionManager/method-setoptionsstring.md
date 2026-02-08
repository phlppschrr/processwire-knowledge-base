# $selectableOptionManager->setOptionsString(Field $field, $value, $allowDelete = true): array

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionManager.php`

Set an options string

Should adhere to the format

One option per line in the format: 123=title or 123=value|title
where 123 is the option ID, 'value' is an optional value,
and 'title' is a required title.

For new options, specify just the option title
(or value|title) on its own line. Options should
be in the desired sort order.

## Arguments

- `$field` `Field`
- `$value` `string`
- `$allowDelete` (optional) `bool` Allow removed lines in the string to result in deleted options? If false, no options will be affected but you can call the getRemovedOptionIDs() method to retrieve them for confirmation.

## Return value

array containing ('added' => cnt, 'updated' => cnt, 'deleted' => cnt, 'marked' => cnt) note: 'marked' means marked for deletion
