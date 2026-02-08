# $wireSaveableItems->delete(Saveable $item): bool

Source: `wire/core/WireSaveableItems.php`

Delete the provided item from the database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItems->delete($item);

// usage with all arguments
$bool = $wireSaveableItems->delete(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `delete`
- Implementation: `___delete`
- Hook with: `$wireSaveableItems->delete()`

## Arguments

- `$item` `Saveable` Item to save

## Return value

- `bool` Returns true on success, false on failure

## Exceptions

- `WireException`
