# $fieldtype->getMatchQuery($query, $table, $subfield, $operator, $value): PageFinderDatabaseQuerySelect|DatabaseQuerySelect

Source: `wire/core/Fieldtype.php`

Get the database query that matches a Fieldtype table’s data with a given value.

Possible template method: If overridden, children do not need to call this method
if they update the $query themselves.

Note the following additional properties are available from the $query argument:

 - `$query->field` (Field): Field instance that being referred to match.
 - `$query->group` (string): Original group of the field in the selector (when applicable).
 - `$query->selector` (Selector): Original Selector object (matching the $field).
 - `$query->selectors` (Selectors): Original Selectors object (matching $field and others).
 - `$query->parentQuery` (DatabaseQuerySelect): Parent database query that $query will be merged into.
 - `$query->pageFinder` (PageFinder): The PageFinder instance that initiated the query, for additional info.

## Arguments

- `$query` `PageFinderDatabaseQuerySelect`
- `$table` `string` The table name to use
- `$subfield` `string` Name of the subfield (typically 'data', unless selector explicitly specified another)
- `$operator` `string` The comparison operator. - This base Fieldtype class accepts only database operators (=, !=, >, >=, <, <=, &). - Other Fieldtypes may choose to accept more operators according to need of Fieldtype.
- `$value` `mixed` Value to find. - If given array, this base Fieldtype class (only) will match via OR condition. (3.0.182+) - Other Fieldtypes may choose to interpret array values differently according need of Fieldtype.

## Return value

PageFinderDatabaseQuerySelect|DatabaseQuerySelect $query

## Throws

- WireException
