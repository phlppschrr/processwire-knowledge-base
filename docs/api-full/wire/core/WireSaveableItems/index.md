# WireSaveableItems

Source: `wire/core/WireSaveableItems.php`

Inherits: `Wire`
Implements: `IteratorAggregate`

## Summary

ProcessWire WireSaveableItems

Common methods:
- [`getAll()`](method-getall.md)
- [`makeBlankItem()`](method-makeblankitem.md)
- [`getWireArray()`](method-getwirearray.md)
- [`makeItem()`](method-makeitem.md)
- [`getTable()`](method-gettable.md)

Groups:
Group: [other](group-other.md)

Wire Data Access Object, provides reusable capability for loading, saving, creating, deleting,
and finding items of descending class-defined types.

## Methods
- [`getAll(): WireArray`](method-getall.md) Return the WireArray that this DAO stores it's items in
- [`makeBlankItem(): Saveable|Wire`](method-makeblankitem.md) Return a new blank item
- [`makeItem(array $a = array()): Saveable|WireData|Wire`](method-makeitem.md) Make an item and populate with given data
- [`getTable(): string`](method-gettable.md) Return the name of the table that this DAO stores item records in
- [`getSort(): string`](method-getsort.md) Return the default name of the field that load() should sort by (default is none)
- [`getLoadQuerySelectors(Selectors $selectors, DatabaseQuerySelect $query): DatabaseQuerySelect`](method-getloadqueryselectors.md) Provides additions to the ___load query for when selectors or selector string are provided
- [`getLoadQuery(Selectors|string|null $selectors = null): DatabaseQuerySelect`](method-getloadquery.md) Get the DatabaseQuerySelect to perform the load operation of items
- [`load(WireArray $items, Selectors|string|null $selectors = null): WireArray`](method-___load.md) (hookable) Load items from the database table and return them in the same type class that getAll() returns
- [`loadRowsReady(array &$rows)`](method-loadrowsready.md) Called after rows loaded from DB but before populated to this instance
- [`initItem(array &$row, ?WireArray $items = null): Saveable|WireData|Wire`](method-inititem.md) Create a new Saveable item from a raw array ($row) and add it to $items
- [`saveItemKey(string $key): bool`](method-saveitemkey.md) Should the given item key/field be saved in the database?
- [`save(Saveable $item): bool`](method-___save.md) (hookable) Save the provided item to database
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable) Delete the provided item from the database
- [`clone(Saveable $item, string $name = ''): bool|Saveable`](method-___clone.md) (hookable) Create and return a cloned copy of this item
- [`find(Selectors|string $selectors): WireArray`](method-___find.md) (hookable) Find items based on Selectors or selector string
- [`get(string|int $key): array|mixed|null|Page|Saveable|Wire|WireData`](method-get.md) Get an item
- [`has(string|int|Saveable|WireData $item): bool`](method-has.md) Do we have the given item or item by given key?
- [`__isset(string|int $key): bool`](method-__isset.md) Isset
- [`encodeData(array $value): string`](method-encodedata.md) Encode the 'data' portion of the table.
- [`decodeData(string $value): array`](method-decodedata.md) Decode the 'data' portion of the table.
- [`useFuel(bool|null $useFuel = null): bool`](method-usefuel.md) Enforce no locally-scoped fuel for this class
- [`saveReady(Saveable $item)`](method-___saveready.md) (hookable) Hook that runs right before item is to be saved.
- [`deleteReady(Saveable $item)`](method-___deleteready.md) (hookable) Hook that runs right before item is to be deleted.
- [`cloneReady(Saveable $item, Saveable $copy)`](method-___cloneready.md) (hookable) Hook that runs right before item is to be cloned.
- [`renameReady(Saveable $item, string $oldName, string $newName)`](method-___renameready.md) (hookable) Hook that runs right before item is to be renamed.
- [`saved(Saveable $item, array $changes = array())`](method-___saved.md) (hookable) Hook that runs right after an item has been saved.
- [`added(Saveable $item)`](method-___added.md) (hookable) Hook that runs right after a new item has been added.
- [`deleted(Saveable $item)`](method-___deleted.md) (hookable) Hook that runs right after an item has been deleted.
- [`cloned(Saveable $item, Saveable $copy)`](method-___cloned.md) (hookable) Hook that runs right after an item has been cloned.
- [`renamed(Saveable $item, string $oldName, string $newName)`](method-___renamed.md) (hookable) Hook that runs right after an item has been renamed.
- [`__invoke($key): Wire|null`](method-__invoke.md) Enables use of $apivar('name') or wire()->apivar('name')
- [`log($str, ?Saveable $item = null): WireLog`](method-log.md) Save to activity log, if enabled in config
- [`error(string $text, int|bool $flags = 0): Wire|WireSaveableItems`](method-error.md) Record an error
- [`__debugInfo(): array`](method-__debuginfo.md) debugInfo PHP 5.6+ magic method
- [`useLazy(): bool`](method-uselazy.md) Use lazy loading for this type?
- [`unsetLazy(Saveable $item): bool`](method-unsetlazy.md) Remove item from lazy loading data/indexes
