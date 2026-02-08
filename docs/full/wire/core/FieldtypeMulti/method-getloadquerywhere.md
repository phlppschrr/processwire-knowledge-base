# $fieldtypeMulti->getLoadQueryWhere(Field $field, DatabaseQuerySelect $query, $col, $operator, $value): DatabaseQuery

Source: `wire/core/FieldtypeMulti.php`

Apply a where condition to a load query (used by getLoadQuery method)

## Arguments

- `$field` `Field`
- `$query` `DatabaseQuerySelect`
- `$col` `string` The column name
- `$operator` `string` The comparison operator
- `$value` `mixed` The value to find

## Return value

DatabaseQuery $query

## Throws

- WireException if given invalid or unrecognized arguments
