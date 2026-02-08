# $fieldtypeMulti->getLoadQueryWhere(Field $field, DatabaseQuerySelect $query, $col, $operator, $value): DatabaseQuery

Source: `wire/core/FieldtypeMulti.php`

Apply a where condition to a load query (used by getLoadQuery method)

## Arguments

- Field $field
- DatabaseQuerySelect $query
- string $col The column name
- string $operator The comparison operator
- mixed $value The value to find

## Return value

DatabaseQuery $query

## Throws

- WireException if given invalid or unrecognized arguments
