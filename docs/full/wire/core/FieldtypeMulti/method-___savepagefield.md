# FieldtypeMulti::___savePageField()

Source: `wire/core/FieldtypeMulti.php`

Per the Fieldtype interface, Save the given Field from the given Page to the database

Because the number of values may have changed, this method plays it safe and deletes all the old values
and reinserts them as new.

@param Page $page

@param Field $field

@return bool

@throws \PDOException|WireException|WireDatabaseQueryException on failure
