# $wireSaveableItemsLookup->save(Saveable $item): bool

Source: `wire/core/WireSaveableItemsLookup.php`

Save the provided item to database

## Usage

~~~~~
// basic usage
$bool = $wireSaveableItemsLookup->save($item);

// usage with all arguments
$bool = $wireSaveableItemsLookup->save(Saveable $item);
~~~~~

## Hookable

- Hookable method name: `save`
- Implementation: `___save`
- Hook with: `$wireSaveableItemsLookup->save()`

## Arguments

- `$item` `Saveable`

## Return value

- `bool`

## Exceptions

- `WireException`
