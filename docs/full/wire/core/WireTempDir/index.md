# WireTempDir

Source: `wire/core/WireTempDir.php`

Inherits: `Wire`

ProcessWire Temporary Directory Manager

Methods:
- [`__construct(string|object $name = '', string $basePath = '')`](method-__construct.md)
- [`__destruct()`](method-__destruct.md)
- [`init(string|object $name = '', string $basePath = ''): string`](method-init.md)
- [`classRootPath(bool $createIfNotExists = false, string $basePath = ''): string`](method-classrootpath.md)
- [`createName(string $prefix = ''): string`](method-createname.md)
- [`setRemove(bool $remove = true): $this`](method-setremove.md)
- [`get(string $id = ''): string`](method-get.md)
- [`remove(): bool`](method-remove.md)
- [`removeExpiredDirs(string $path, $maxAge): bool`](method-removeexpireddirs.md)
- [`getNewestModTime(string $path, int $maxDepth = 5): int`](method-getnewestmodtime.md)
- [`removeAll()`](method-removeall.md)
- [`__toString(): string`](method-__tostring.md)
- [`mkdir(string $dir, bool $recursive = false): bool`](method-mkdir.md)
- [`rmdir(string $dir, bool $recursive = false): bool`](method-rmdir.md)
- [`isTempDir(string $dir): bool`](method-istempdir.md)
- [`maintenance(): bool`](method-maintenance.md)
- [`create(string $name = '', string $basePath = ''): string`](method-create.md)

Constants:
- [`hiddenFileName`](const-hiddenfilename.md)
