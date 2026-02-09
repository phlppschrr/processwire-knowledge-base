# $fieldtypeMulti->getLoadQueryAutojoin(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect|NULL

Source: `wire/core/FieldtypeMulti.php`

Return the query used for Autojoining this field (if different from getLoadQuery) or NULL if autojoin not allowed.

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $fieldtypeMulti->getLoadQueryAutojoin($field, $query);

// usage with all arguments
$databaseQuerySelect = $fieldtypeMulti->getLoadQueryAutojoin(Field $field, DatabaseQuerySelect $query);
~~~~~

## Arguments

- `$field` `Field`
- `$query` `DatabaseQuerySelect`

## Return value

- `DatabaseQuerySelect|NULL`
