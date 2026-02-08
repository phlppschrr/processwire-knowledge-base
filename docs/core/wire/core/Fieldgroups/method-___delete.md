# $fieldgroups->delete(Saveable $item): bool

Source: `wire/core/Fieldgroups.php`

Delete the given fieldgroup from the database

Also deletes the references in fieldgroups_fields table

## Usage

~~~~~
// basic usage
$bool = $fieldgroups->delete($item);

// usage with all arguments
$bool = $fieldgroups->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$fieldgroups->delete()`

## Arguments

- `$item` `Saveable|Fieldgroup`

## Return value

- `bool`

## Exceptions

- `WireException`
