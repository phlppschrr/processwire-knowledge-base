# FieldsTableTools

Source: `wire/core/FieldsTableTools.php`

Methods:
- [`checkUniqueIndex(Field $field, bool $verbose = true)`](method-checkuniqueindex.md) Check state of field unique 'data' index and update as needed
- [`deleteEmptyRows(Field $field, string $col = 'data', bool $strict = true): bool|int`](method-deleteemptyrows.md) Delete rows having empty column value
- [`getUniqueIndexInputfield(Field $field): InputfieldCheckbox`](method-getuniqueindexinputfield.md) Create a checkbox Inputfield to configure unique value state
- [`valueExists(Field $field, string|int $value, string $col = 'data'): int`](method-valueexists.md) Does given value exist anywhere in field table?
