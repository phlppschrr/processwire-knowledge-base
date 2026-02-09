# WireDataDB

Source: `wire/core/WireDataDB.php`

Inherits: `WireData`
Implements: `Countable`

WireData with database storage

A WireData object that maintains its data in a database table rather than just in memory.
An example of usage is the `$page->meta()` method.

Methods:
- [`__construct(int $sourceID, string $tableName)`](method-__construct.md)
- [`get(string $key): array|mixed|null`](method-get.md)
- [`getArray(): array|mixed|null`](method-getarray.md)
- [`set(string $key, mixed $value): self`](method-set.md)
- [`remove(string $key): self`](method-remove.md)
- [`removeAll(): $this`](method-removeall.md)
- [`reset(): $this`](method-reset.md)
- [`delete(string|bool $name): int`](method-delete.md)
- [`load(string|bool $name): array|mixed|null`](method-load.md)
- [`save(string $name, mixed $value, bool $recursive = false): bool`](method-save.md)
- [`sourceID(int|null $id = null): int`](method-sourceid.md)
- [`count(): int`](method-count.md)
- [`copyTo(int $newSourceID): int`](method-copyto.md)
- [`table(string $tableName = ''): string`](method-table.md)
- [`schema(): array`](method-schema.md)
- [`install(): bool`](method-install.md)
- [`uninstall(): bool`](method-uninstall.md)
