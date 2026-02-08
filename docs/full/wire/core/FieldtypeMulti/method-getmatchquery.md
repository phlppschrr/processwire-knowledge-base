# $fieldtypeMulti->getMatchQuery($query, $table, $subfield, $operator, $value): PageFinderDatabaseQuerySelect|DatabaseQuerySelect

Source: `wire/core/FieldtypeMulti.php`

Get the query that matches a Fieldtype table's data with a given value

Possible template method: If overridden, children should NOT call this parent method.

## Arguments

- PageFinderDatabaseQuerySelect $query
- string $table The table name to use
- string $subfield Name of the field (typically 'data', unless selector explicitly specified another)
- string $operator The comparison operator
- mixed $value The value to find

## Return value

PageFinderDatabaseQuerySelect|DatabaseQuerySelect $query
