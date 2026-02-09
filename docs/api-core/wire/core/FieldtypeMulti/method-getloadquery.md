# $fieldtypeMulti->getLoadQuery(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect

Source: `wire/core/FieldtypeMulti.php`

Return the query used for loading all parts of the data from this field.

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $fieldtypeMulti->getLoadQuery($field, $query);

// usage with all arguments
$databaseQuerySelect = $fieldtypeMulti->getLoadQuery(Field $field, DatabaseQuerySelect $query);
~~~~~

## Arguments

- `$field` `Field`
- `$query` `DatabaseQuerySelect`

## Return value

- `DatabaseQuerySelect`

## Exceptions

- `WireException`
