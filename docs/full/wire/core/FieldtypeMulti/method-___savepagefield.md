# $fieldtypeMulti->___savePageField(Page $page, Field $field): bool

Source: `wire/core/FieldtypeMulti.php`

Per the Fieldtype interface, Save the given Field from the given Page to the database

Because the number of values may have changed, this method plays it safe and deletes all the old values
and reinserts them as new.

## Usage

~~~~~
// basic usage
$bool = $fieldtypeMulti->___savePageField($page, $field);

// usage with all arguments
$bool = $fieldtypeMulti->___savePageField(Page $page, Field $field);
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`

## Return value

- `bool`

## Exceptions

- `\PDOException|WireException|WireDatabaseQueryException` on failure
