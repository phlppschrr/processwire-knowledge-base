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
- [`__construct(string $path, string|int $id, int $cacheTimeSeconds)`](method-__construct.md) Construct the CacheFile
- [`setSecondaryID(string|int $id)`](method-setsecondaryid.md) An extra part to be appended to the filename
- [`buildFilename(): string`](method-buildfilename.md) Build a filename for use by the cache
- [`exists(): bool`](method-exists.md) Does the cache file exist?
- [`get(): string`](method-get.md) Get the contents of the cache based on the primary or secondary ID
- [`isCacheFileExpired(string $filename): bool`](method-iscachefileexpired.md) Is the given cache filename expired?
- [`save(string $data): bool`](method-save.md) Saves $data to the cache
- [`remove()`](method-remove.md) Removes all cache files for primaryID
- [`removeFilename(string $filename)`](method-removefilename.md) Removes just the given file, as opposed to remove() which removes the entire cache for primaryID
- [`expireAll()`](method-expireall.md) Causes all cache files in this type to be immediately expired
- [`setChmodFile(string $mode)`](method-setchmodfile.md) Set the octal mode for files created by CacheFile
- [`setChmodDir(string $mode)`](method-setchmoddir.md) Set the octal mode for dirs created by CacheFile
- [`__toString()`](method-__tostring.md) CacheFile classes return a string of their cache filename

Constants:
- [`maxCacheFiles = 999`](const-maxcachefiles.md)
