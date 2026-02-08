# FieldsTableTools

Source: `wire/core/FieldsTableTools.php`


## checkUniqueIndex()

Check state of field unique 'data' index and update as needed

@param Field $field

@param bool $verbose Show messages when changes made? (default=true)

@throws WireException

## deleteEmptyRows()

Delete rows having empty column value

@param Field $field

@param string $col Column name (default='data')

@param bool $strict When true, delete not allowed if there are columns other than one given and 'pages_id' (default=true)

@return bool|int Returns false if delete not allowed, otherwise returns int with # of rows deleted

@throws WireException

## getUniqueIndexInputfield()

Create a checkbox Inputfield to configure unique value state

@param Field $field

@return InputfieldCheckbox

## valueExists()

Does given value exist anywhere in field table?

@param Field $field

@param string|int $value

@param string $col

@return int Returns page ID where value exists, if found. Otherwise returns 0.

@throws WireException
