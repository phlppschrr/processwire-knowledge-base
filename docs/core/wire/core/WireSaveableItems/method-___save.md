# $wireSaveableItems->save(Saveable $item): bool

Source: `wire/core/WireSaveableItems.php`

Save the provided item to database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItems->save($item);

// usage with all arguments
$bool = $wireSaveableItems->save(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$wireSaveableItems->save()`

## Arguments

- `$item` `Saveable` The item to save

## Return value

- `bool` Returns true on success, false on failure

## Exceptions

- `WireException`
