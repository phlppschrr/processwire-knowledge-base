# WireCacheInterface

Source: `wire/core/Interfaces.php`

Interface for WireCache handler classes

For example implementations of this interface see
WireCacheDatabase (core) and WireCacheFilesystem (module)

@since 3.0.218

Methods:
- [`find(array $options): array`](method-find.md)
- [`save(string $name, string $data, string $expire): bool`](method-save.md)
- [`delete(string $name): bool`](method-delete.md)
- [`deleteAll(): int`](method-deleteall.md)
- [`expireAll(): int`](method-expireall.md)
