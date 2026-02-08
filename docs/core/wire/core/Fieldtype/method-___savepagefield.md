# Fieldtype::___savePageField()

Source: `wire/core/Fieldtype.php`

Save the given field from given page to the database.

Possible template method: If overridden, it is likely not necessary to call this parent method.


@param Page $page Page object to save.

@param Field $field Field to retrieve from the page.

@return bool True on success, false on DB save failure.

@throws WireException|\PDOException|WireDatabaseException
