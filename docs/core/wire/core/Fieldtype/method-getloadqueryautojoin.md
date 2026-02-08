# Fieldtype::getLoadQueryAutojoin()

Source: `wire/core/Fieldtype.php`

Return the query used for Autojoining this field (if different from getLoadQuery) or NULL if autojoin not allowed.


@param Field $field

@param DatabaseQuerySelect $query

@return DatabaseQuerySelect|NULL
