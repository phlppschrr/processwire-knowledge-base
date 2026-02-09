# WireSaveableItems

Source: `wire/core/WireSaveableItems.php`

Inherits: `Wire`
Implements: `IteratorAggregate`


Groups:
Group: [other](group-other.md)

ProcessWire WireSaveableItems

Wire Data Access Object, provides reusable capability for loading, saving, creating, deleting,
and finding items of descending class-defined types.

Methods:
- [`getAll(): WireArray`](method-getall.md)
- [`makeBlankItem(): Saveable|Wire`](method-makeblankitem.md)
- [`makeItem(array $a = array()): Saveable|WireData|Wire`](method-makeitem.md)
- [`getTable(): string`](method-gettable.md)
- [`getSort(): string`](method-getsort.md)
- [`getLoadQuerySelectors(Selectors $selectors, DatabaseQuerySelect $query): DatabaseQuerySelect`](method-getloadqueryselectors.md)
- [`getLoadQuery(Selectors|string|null $selectors = null): DatabaseQuerySelect`](method-getloadquery.md)
- [`load(WireArray $items, Selectors|string|null $selectors = null): WireArray`](method-___load.md) (hookable)
- [`loadRowsReady(array &$rows)`](method-loadrowsready.md)
- [`initItem(array &$row, ?WireArray $items = null): Saveable|WireData|Wire`](method-inititem.md)
- [`saveItemKey(string $key): bool`](method-saveitemkey.md)
- [`save(Saveable $item): bool`](method-___save.md) (hookable)
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable)
- [`clone(Saveable $item, string $name = ''): bool|Saveable`](method-___clone.md) (hookable)
- [`find(Selectors|string $selectors): WireArray`](method-___find.md) (hookable)
- [`get(string|int $key): array|mixed|null|Page|Saveable|Wire|WireData`](method-get.md)
- [`has(string|int|Saveable|WireData $item): bool`](method-has.md)
- [`__isset(string|int $key): bool`](method-__isset.md)
- [`encodeData(array $value): string`](method-encodedata.md)
- [`decodeData(string $value): array`](method-decodedata.md)
- [`useFuel(bool|null $useFuel = null): bool`](method-usefuel.md)
- [`saveReady(Saveable $item)`](method-___saveready.md) (hookable)
- [`saveReady(Saveable $item)`](method-___saveready.md) (hookable)
- [`deleteReady(Saveable $item)`](method-___deleteready.md) (hookable)
- [`cloneReady(Saveable $item, Saveable $copy)`](method-___cloneready.md) (hookable)
- [`renameReady(Saveable $item, string $oldName, string $newName)`](method-___renameready.md) (hookable)
- [`saved(Saveable $item, array $changes = array())`](method-___saved.md) (hookable)
- [`added(Saveable $item)`](method-___added.md) (hookable)
- [`deleted(Saveable $item)`](method-___deleted.md) (hookable)
- [`cloned(Saveable $item, Saveable $copy)`](method-___cloned.md) (hookable)
- [`renamed(Saveable $item, string $oldName, string $newName)`](method-___renamed.md) (hookable)
- [`__invoke($key)`](method-__invoke.md)
- [`__invoke($key): Wire|null`](method-__invoke.md)
- [`log($str, ?Saveable $item = null): WireLog`](method-log.md)
- [`error(string $text, int|bool $flags = 0): Wire|WireSaveableItems`](method-error.md)
- [`__debugInfo(): array`](method-__debuginfo.md)
- [`useLazy(): bool`](method-uselazy.md)
- [`unsetLazy(Saveable $item): bool`](method-unsetlazy.md)
