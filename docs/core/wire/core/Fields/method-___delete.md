# $fields->___delete(Saveable $item): bool

Source: `wire/core/Fields.php`

Delete a Field from the database

This method will throw a WireException if you attempt to delete a field that is currently in use (i.e. assigned to one or more fieldgroups).

## Arguments

- Field $item Field to delete

## Return value

bool True on success, false on failure

## Throws

- WireException
