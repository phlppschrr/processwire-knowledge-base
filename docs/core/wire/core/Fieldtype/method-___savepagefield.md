# $fieldtype->___savePageField(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Save the given field from given page to the database.

Possible template method: If overridden, it is likely not necessary to call this parent method.

## Arguments

- Page $page Page object to save.
- Field $field Field to retrieve from the page.

## Return value

bool True on success, false on DB save failure.

## Throws

- WireException|\PDOException|WireDatabaseException
