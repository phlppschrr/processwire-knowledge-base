# $wireSaveableItems->___delete(Saveable $item): bool

Source: `wire/core/WireSaveableItems.php`

Delete the provided item from the database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItems->___delete($item);

// usage with all arguments
$bool = $wireSaveableItems->___delete(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable` Item to save

## Return value

- `bool` Returns true on success, false on failure

## Exceptions

- `WireException`
