# $wireSaveableItemsLookup->load(WireArray $items, $selectors = null): WireArray

Source: `wire/core/WireSaveableItemsLookup.php`

Load items from the database table and return them in the same type class that getAll() returns

A selector string or Selectors may be provided so that this can be used as a find() by descending classes that don't load all items at once.

## Usage

~~~~~
// basic usage
$items = $wireSaveableItemsLookup->load($items);

// usage with all arguments
$items = $wireSaveableItemsLookup->load(WireArray $items, $selectors = null);
~~~~~

## Hookable

- Hookable method name: `load`
- Implementation: `___load`
- Hook with: `$wireSaveableItemsLookup->load()`

## Arguments

- `$items` `WireArray`
- `$selectors` (optional) `Selectors|string|null` Selectors or a selector string to find, or NULL to load all.

## Return value

- `WireArray` Returns the same type as specified in the getAll() method.
