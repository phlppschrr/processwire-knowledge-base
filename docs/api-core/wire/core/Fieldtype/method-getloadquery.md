# $fieldtype->getLoadQuery(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect

Source: `wire/core/Fieldtype.php`

Return the query used for loading all parts of the data from this field.

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $fieldtype->getLoadQuery($field, $query);

// usage with all arguments
$databaseQuerySelect = $fieldtype->getLoadQuery(Field $field, DatabaseQuerySelect $query);
~~~~~

## Arguments

- `$field` `Field`
- `$query` `DatabaseQuerySelect`

## Return value

- `DatabaseQuerySelect`
