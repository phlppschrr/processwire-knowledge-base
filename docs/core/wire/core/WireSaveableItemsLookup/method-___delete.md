# $wireSaveableItemsLookup->delete(Saveable $item): bool

Source: `wire/core/WireSaveableItemsLookup.php`

Delete the provided item from the database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItemsLookup->delete($item);

// usage with all arguments
$bool = $wireSaveableItemsLookup->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$wireSaveableItemsLookup->delete()`

## Arguments

- `$item` `Saveable`

## Return value

- `bool`
