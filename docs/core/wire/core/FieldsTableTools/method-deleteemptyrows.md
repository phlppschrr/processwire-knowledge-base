# FieldsTableTools::deleteEmptyRows()

Source: `wire/core/FieldsTableTools.php`

Delete rows having empty column value

@param Field $field

@param string $col Column name (default='data')

@param bool $strict When true, delete not allowed if there are columns other than one given and 'pages_id' (default=true)

@return bool|int Returns false if delete not allowed, otherwise returns int with # of rows deleted

@throws WireException
