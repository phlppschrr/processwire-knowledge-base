# WireDataDB

Source: `wire/core/WireDataDB.php`

Inherits: `WireData`
Implements: `Countable`

WireData with database storage

A WireData object that maintains its data in a database table rather than just in memory.
An example of usage is the `$page->meta()` method.

Methods:
- [`__construct(int $sourceID, string $tableName)`](method-__construct.md) Construct
- [`get(string $key): array|mixed|null`](method-get.md) Get the value for a specific property/name/key
- [`getArray(): array|mixed|null`](method-getarray.md) Get all values in an associative array
- [`set(string $key, mixed $value): self`](method-set.md) Set and save a value for a specific property/name/key
- [`remove(string $key): self`](method-remove.md) Remove value for a specific property/name/key
- [`removeAll(): $this`](method-removeall.md) Remove all values for sourceID from the DB
- [`reset(): $this`](method-reset.md) Reset all loaded data so that it will re-load from DB on next access
- [`delete(string|bool $name): int`](method-delete.md) Delete meta value or all meta values (if you specify true)
- [`load(string|bool $name): array|mixed|null`](method-load.md) Load a value or all values
- [`save(string $name, mixed $value, bool $recursive = false): bool`](method-save.md) Save a value
- [`sourceID(int|null $id = null): int`](method-sourceid.md) Get or set the the source ID for this instance
- [`count(): int`](method-count.md) Count the number of rows this WireDataDB maintains in the database for source ID.
- [`copyTo(int $newSourceID): int`](method-copyto.md) Copy all data to a new source ID
- [`table(string $tableName = ''): string`](method-table.md) Get the current table name
- [`schema(): array`](method-schema.md) Get DB schema in an array
- [`install(): bool`](method-install.md) Install the table
- [`uninstall(): bool`](method-uninstall.md) Uninstall the table
