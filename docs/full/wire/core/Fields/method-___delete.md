# $fields->delete(Saveable $item): bool

Source: `wire/core/Fields.php`

Delete a Field from the database

This method will throw a WireException if you attempt to delete a field that is currently in use (i.e. assigned to one or more fieldgroups).

## Usage

~~~~~
// basic usage
$bool = $fields->delete($item);

// usage with all arguments
$bool = $fields->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$fields->delete()`

## Arguments

- `$item` `Field` Field to delete

## Return value

- `bool` True on success, false on failure

## Exceptions

- `WireException`
