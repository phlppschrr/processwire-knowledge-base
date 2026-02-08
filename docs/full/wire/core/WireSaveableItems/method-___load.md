# $wireSaveableItems->___load(WireArray $items, $selectors = null): WireArray

Source: `wire/core/WireSaveableItems.php`

Load items from the database table and return them in the same type class that getAll() returns

A selector string or Selectors may be provided so that this can be used as a find() by descending classes that don't load all items at once.

## Arguments

- WireArray $items
- Selectors|string|null $selectors Selectors or a selector string to find, or NULL to load all.

## Return value

WireArray Returns the same type as specified in the getAll() method.
