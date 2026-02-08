# WireSaveableItems::___load()

Source: `wire/core/WireSaveableItems.php`

Load items from the database table and return them in the same type class that getAll() returns

A selector string or Selectors may be provided so that this can be used as a find() by descending classes that don't load all items at once.

@param WireArray $items

@param Selectors|string|null $selectors Selectors or a selector string to find, or NULL to load all.

@return WireArray Returns the same type as specified in the getAll() method.
