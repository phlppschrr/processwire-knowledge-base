# FieldtypeMulti::getMatchQuery()

Source: `wire/core/FieldtypeMulti.php`

Get the query that matches a Fieldtype table's data with a given value

Possible template method: If overridden, children should NOT call this parent method.

@param PageFinderDatabaseQuerySelect $query

@param string $table The table name to use

@param string $subfield Name of the field (typically 'data', unless selector explicitly specified another)

@param string $operator The comparison operator

@param mixed $value The value to find

@return PageFinderDatabaseQuerySelect|DatabaseQuerySelect $query
