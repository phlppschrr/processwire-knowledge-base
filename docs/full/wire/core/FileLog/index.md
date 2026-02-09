# FileLog

Source: `wire/core/FileLog.php`

Inherits: `Wire`

ProcessWire FileLog

Creates and maintains a text-based log file.

Methods:
- [`__construct(string $path, string $identifier = '')`](method-__construct.md) Construct the FileLog
- [`wired()`](method-wired.md) Wired to API
- [`__get(string $name): mixed`](method-__get.md)
- [`cleanStr($str): string`](method-cleanstr.md) Clean a string for use in a log file entry
- [`save(string $str, array $options = array()): bool`](method-save.md) Save the given log entry string
- [`removeLineFromChunk(string &$line, string &$chunk, int $chunkSize)`](method-removelinefromchunk.md) Remove given $line from $chunk and add counter to end of $line indicating quantity that was removed
- [`size(): int|false`](method-size.md) Get filesize
- [`filename(): string`](method-filename.md) Get file basename
- [`pathname(): string|bool`](method-pathname.md) Get file pathname
- [`mtime(): int|false`](method-mtime.md) Get file modification time
- [`get(int $chunkSize = 0, int $chunkNum = 1): array`](method-get.md) Get lines from the end of a file based on chunk size (deprecated)
- [`getChunkArray(int $chunkNum = 1, int $chunkSize = 0, bool $reverse = true): array`](method-getchunkarray.md) Get lines from the end of a file based on chunk size
- [`getChunk(int $chunkNum = 1, int $chunkSize = 0, bool $reverse = true, bool $clean = true): string`](method-getchunk.md) Get a chunk of data (string) from the end of the log file
- [`getTotalChunks(int $chunkSize = 0): int`](method-gettotalchunks.md) Get the total number of chunks in the file
- [`getTotalLines(): int`](method-gettotallines.md) Get total number of lines in the log file
- [`getDate(int $dateFrom, int $dateTo = 0, int $pageNum = 1, int $limit = 100): array`](method-getdate.md) Get log lines that lie within a date range
- [`find(int $limit = 100, int $pageNum = 1, array $options = array()): int|array`](method-find.md) Return lines from the end of the log file, with various options
- [`isValidLine($line, array $options, bool &$stopNow): bool`](method-isvalidline.md) Returns whether the given log line is valid to be considered a log entry
- [`prune($bytes): bool|int`](method-prune.md) Prune to number of bytes
- [`pruneBytes(int $bytes): int|bool`](method-prunebytes.md) Prune log file to specified number of bytes (from the end)
- [`pruneDate(int|string $oldestDate): int`](method-prunedate.md) Prune log file to contain only entries newer than $oldestDate
- [`delete(): bool`](method-delete.md) Delete the log file
- [`chunkSize(int $chunkSize = 0): int`](method-chunksize.md) Get or set the default chunk size used when reading from logs and not overridden by method argument
- [`path(): string`](method-path.md) Get path where the log is stored (with trailing slash)

Constants:
- [`defaultChunkSize`](const-defaultchunksize.md)
- [`debug`](const-debug.md)
