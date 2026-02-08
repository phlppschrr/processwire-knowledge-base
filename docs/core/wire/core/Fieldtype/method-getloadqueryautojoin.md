# $fieldtype->getLoadQueryAutojoin(Field $field, DatabaseQuerySelect $query): DatabaseQuerySelect|NULL

Source: `wire/core/Fieldtype.php`

Return the query used for Autojoining this field (if different from getLoadQuery) or NULL if autojoin not allowed.

## Arguments

- `$field` `Field`
- `$query` `DatabaseQuerySelect`

## Return value

DatabaseQuerySelect|NULL
