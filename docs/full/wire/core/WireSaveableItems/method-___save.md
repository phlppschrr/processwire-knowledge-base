# $wireSaveableItems->___save(Saveable $item): bool

Source: `wire/core/WireSaveableItems.php`

Save the provided item to database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItems->___save($item);

// usage with all arguments
$bool = $wireSaveableItems->___save(Saveable $item);
~~~~~

## Arguments

- `$item` `Saveable` The item to save

## Return value

- `bool` Returns true on success, false on failure

## Exceptions

- `WireException`
