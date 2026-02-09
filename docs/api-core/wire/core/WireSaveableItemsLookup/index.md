# WireSaveableItemsLookup

Source: `wire/core/WireSaveableItemsLookup.php`

Inherits: `WireSaveableItems`

ProcessWire WireSaveableItemsLookup

Provides same functionality as WireSaveableItems except that this class includes joining/modification of a related lookup table

Methods:
- [`getLookupTable()`](method-getlookuptable.md) If a lookup table should be left joined, this method should return the table name
- [`getLookupField()`](method-getlookupfield.md) If a lookup table should be left joined, this method returns the name of the array field in $data that contains multiple values
- [`getLoadQuery(Selectors|string|null $selectors = null): DatabaseQuerySelect`](method-getloadquery.md) Get the DatabaseQuerySelect to perform the load operation of items
- [`load(WireArray $items, Selectors|string|null $selectors = null): WireArray`](method-___load.md) (hookable) Load items from the database table and return them in the same type class that getAll() returns
- [`initItem(array &$row, ?WireArray $items = null): Saveable|HasLookupItems|WireData|Wire`](method-inititem.md) Create a new Saveable/Lookup item from a raw array ($row) and add it to $items
- [`saveItemKey(string $key): bool`](method-saveitemkey.md) Should the given item key/field be saved in the database?
- [`save(Saveable $item): bool`](method-___save.md) (hookable) Save the provided item to database
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable) Delete the provided item from the database
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method
