# $fieldgroups->___delete(Saveable $item): bool

Source: `wire/core/Fieldgroups.php`

Delete the given fieldgroup from the database

Also deletes the references in fieldgroups_fields table

## Usage

~~~~~
// basic usage
$bool = $fieldgroups->___delete($item);

// usage with all arguments
$bool = $fieldgroups->___delete(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable|Fieldgroup`

## Return value

- `bool`

## Exceptions

- `WireException`
