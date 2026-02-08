# $fieldtypeMulti->getMatchQuery($query, $table, $subfield, $operator, $value): PageFinderDatabaseQuerySelect|DatabaseQuerySelect

Source: `wire/core/FieldtypeMulti.php`

Get the query that matches a Fieldtype table's data with a given value

Possible template method: If overridden, children should NOT call this parent method.

## Usage

~~~~~
// basic usage
$pageFinderDatabaseQuerySelect = $fieldtypeMulti->getMatchQuery($query, $table, $subfield, $operator, $value);
~~~~~

## Arguments

- `$query` `PageFinderDatabaseQuerySelect`
- `$table` `string` The table name to use
- `$subfield` `string` Name of the field (typically 'data', unless selector explicitly specified another)
- `$operator` `string` The comparison operator
- `$value` `mixed` The value to find

## Return value

- `PageFinderDatabaseQuerySelect|DatabaseQuerySelect` $query
