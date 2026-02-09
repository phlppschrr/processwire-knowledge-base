# WireCacheInterface

Source: `wire/core/Interfaces.php`

## Summary

Interface for WireCache handler classes

Common methods:
- [`find()`](method-find.md)
- [`save()`](method-save.md)
- [`delete()`](method-delete.md)
- [`deleteAll()`](method-deleteall.md)
- [`expireAll()`](method-expireall.md)

For example implementations of this interface see
WireCacheDatabase (core) and WireCacheFilesystem (module)

@since 3.0.218

## Methods
- [`find(array $options): array`](method-find.md) Find caches by names and/or expirations and return requested values
- [`save(string $name, string $data, string $expire): bool`](method-save.md) Save a cache
- [`delete(string $name): bool`](method-delete.md) Delete cache by name
- [`deleteAll(): int`](method-deleteall.md) Delete all caches (except those reserved by the system)
- [`expireAll(): int`](method-expireall.md) Expire all caches (except those that should never expire)
