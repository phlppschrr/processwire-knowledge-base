# Fields::___delete()

Source: `wire/core/Fields.php`

Delete a Field from the database

This method will throw a WireException if you attempt to delete a field that is currently in use (i.e. assigned to one or more fieldgroups).

@param Field $item Field to delete

@return bool True on success, false on failure

@throws WireException
