# $fieldtype->___savePageField(Page $page, Field $field): bool

Source: `wire/core/Fieldtype.php`

Save the given field from given page to the database.

Possible template method: If overridden, it is likely not necessary to call this parent method.

## Usage

~~~~~
// basic usage
$bool = $fieldtype->___savePageField($page, $field);

// usage with all arguments
$bool = $fieldtype->___savePageField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page` Page object to save.
- `$field` `Field` Field to retrieve from the page.

## Return value

- `bool` True on success, false on DB save failure.

## Exceptions

- `WireException|\PDOException|WireDatabaseException`
