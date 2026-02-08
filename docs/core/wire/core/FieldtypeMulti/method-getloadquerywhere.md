# FieldtypeMulti::getLoadQueryWhere()

Source: `wire/core/FieldtypeMulti.php`

Apply a where condition to a load query (used by getLoadQuery method)

@param Field $field

@param DatabaseQuerySelect $query

@param string $col The column name

@param string $operator The comparison operator

@param mixed $value The value to find

@return DatabaseQuery $query

@throws WireException if given invalid or unrecognized arguments
