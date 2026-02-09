# WireTempDir

Source: `wire/core/WireTempDir.php`

Inherits: `Wire`

ProcessWire Temporary Directory Manager

Methods:
- [`__construct(string|object $name = '', string $basePath = '')`](method-__construct.md) Construct
- [`__destruct()`](method-__destruct.md) Destruct
- [`init(string|object $name = '', string $basePath = ''): string`](method-init.md) Initialize temporary directory
- [`classRootPath(bool $createIfNotExists = false, string $basePath = ''): string`](method-classrootpath.md) Return the class root path for cache files (i.e. /path/to/site/assets/cache/WireTempDir/)
- [`createName(string $prefix = ''): string`](method-createname.md) Create a randomized name for runtime temp dir
- [`setRemove(bool $remove = true): $this`](method-setremove.md) Call this with 'false' to prevent temp dir from being removed automatically when object is destructed
- [`get(string $id = ''): string`](method-get.md) Returns a temporary directory (path)
- [`remove(): bool`](method-remove.md) Removes the temporary directory created by this object
- [`removeExpiredDirs(string $path, $maxAge): bool`](method-removeexpireddirs.md) Remove expired directories in the given $path
- [`getNewestModTime(string $path, int $maxDepth = 5): int`](method-getnewestmodtime.md) Get the newest modification time of a file in $path, recursively
- [`removeAll()`](method-removeall.md) Clear all temporary directories created by this class
- [`__toString(): string`](method-__tostring.md) Accessing this object as a string returns the temp dir
- [`mkdir(string $dir, bool $recursive = false): bool`](method-mkdir.md) Create a temporary directory
- [`rmdir(string $dir, bool $recursive = false): bool`](method-rmdir.md) Remove a temporary directory
- [`isTempDir(string $dir): bool`](method-istempdir.md) Is given directory/path created by this class?
- [`maintenance(): bool`](method-maintenance.md) Perform maintenance by cleaning up old temporary directories
- [`create(string $name = '', string $basePath = ''): string`](method-create.md)

Constants:
- [`hiddenFileName`](const-hiddenfilename.md)
