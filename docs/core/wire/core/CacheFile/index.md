# CacheFile

Source: `wire/core/CacheFile.php`

Inherits: `Wire`

ProcessWire CacheFile

Class to manage individual cache files

Each cache file creates it's own directory based on the '$id' given.
The dir is created so that secondary cache files can be created too,
and these are automatically removed when the remove() method is called.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

Methods:
- [`__construct(string $path, string|int $id, int $cacheTimeSeconds)`](method-__construct.md)
- [`setSecondaryID(string|int $id)`](method-setsecondaryid.md)
- [`buildFilename(): string`](method-buildfilename.md)
- [`exists(): bool`](method-exists.md)
- [`get(): string`](method-get.md)
- [`isCacheFileExpired(string $filename): bool`](method-iscachefileexpired.md)
- [`save(string $data): bool`](method-save.md)
- [`remove()`](method-remove.md)
- [`removeFilename(string $filename)`](method-removefilename.md)
- [`expireAll()`](method-expireall.md)
- [`setChmodFile(string $mode)`](method-setchmodfile.md)
- [`setChmodDir(string $mode)`](method-setchmoddir.md)
- [`__toString()`](method-__tostring.md)

Constants:
- [`maxCacheFiles`](const-maxcachefiles.md)
