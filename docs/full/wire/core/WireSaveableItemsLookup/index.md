# WireSaveableItemsLookup

Source: `wire/core/WireSaveableItemsLookup.php`

Inherits: `WireSaveableItems`

ProcessWire WireSaveableItemsLookup

Provides same functionality as WireSaveableItems except that this class includes joining/modification of a related lookup table

Methods:
- [`getLookupTable()`](method-getlookuptable.md)
- [`getLookupField()`](method-getlookupfield.md)
- [`getLoadQuery(Selectors|string|null $selectors = null): DatabaseQuerySelect`](method-getloadquery.md)
- [`load(WireArray $items, Selectors|string|null $selectors = null): WireArray`](method-___load.md) (hookable)
- [`initItem(array &$row, ?WireArray $items = null): Saveable|HasLookupItems|WireData|Wire`](method-inititem.md)
- [`saveItemKey(string $key): bool`](method-saveitemkey.md)
- [`save(Saveable $item): bool`](method-___save.md) (hookable)
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable)
- [`__debugInfo(): array`](method-__debuginfo.md)
