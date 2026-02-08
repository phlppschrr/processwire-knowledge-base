# $fieldsTableTools->deleteEmptyRows(Field $field, $col = 'data', $strict = true): bool|int

Source: `wire/core/FieldsTableTools.php`

Delete rows having empty column value

## Arguments

- `$field` `Field`
- `$col` (optional) `string` Column name (default='data')
- `$strict` (optional) `bool` When true, delete not allowed if there are columns other than one given and 'pages_id' (default=true)

## Return value

bool|int Returns false if delete not allowed, otherwise returns int with # of rows deleted

## Throws

- WireException
