# WireCacheDatabase

Source: `wire/core/WireCacheDatabase.php`

Inherits: `Wire`
Implements: `WireCacheInterface`

Database cache handler for WireCache


@since 2.0.218

Methods:
- [`find(array $options): array`](method-find.md)
- [`save(string $name, string $data, string $expire): bool`](method-save.md)
- [`delete(string $name): bool`](method-delete.md)
- [`deleteAll(): int`](method-deleteall.md)
- [`expireAll(): int`](method-expireall.md)
- [`_deleteAll(bool $expireAll = false): int`](method-_deleteall.md)
- [`executeQuery(\PDOStatement $query): bool`](method-executequery.md)
- [`maintenance(Template|Page $obj): bool`](method-maintenance.md)
- [`install()`](method-install.md)
