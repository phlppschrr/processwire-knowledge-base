# WireCacheDatabase

Source: `wire/core/WireCacheDatabase.php`

Inherits: `Wire`
Implements: `WireCacheInterface`

## Summary

Database cache handler for WireCache

Common methods:
- [`find()`](method-find.md)
- [`save()`](method-save.md)
- [`delete()`](method-delete.md)
- [`deleteAll()`](method-deleteall.md)
- [`expireAll()`](method-expireall.md)

@since 2.0.218

## Methods
- [`find(array $options): array`](method-find.md) Find caches by names or expirations and return requested values
- [`save(string $name, string $data, string $expire): bool`](method-save.md) Save a cache
- [`delete(string $name): bool`](method-delete.md) Delete a cache by name
- [`deleteAll(): int`](method-deleteall.md) Delete all caches (except those reserved by the system)
- [`expireAll(): int`](method-expireall.md) Expire all caches (except those that should never expire)
- [`_deleteAll(bool $expireAll = false): int`](method-_deleteall.md) Implementation for deleteAll and expireAll methods
- [`executeQuery(\PDOStatement $query): bool`](method-executequery.md) Execute query
- [`maintenance(Template|Page $obj): bool`](method-maintenance.md) Database cache maintenance (every 10 minutes)
- [`install()`](method-install.md) Create the caches table if it happens to have been deleted
