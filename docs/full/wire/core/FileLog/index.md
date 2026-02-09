# FileLog

Source: `wire/core/FileLog.php`

Inherits: `Wire`

ProcessWire FileLog

Creates and maintains a text-based log file.

Methods:
- [`__construct(string $path, string $identifier = '')`](method-__construct.md)
- [`wired()`](method-wired.md)
- [`__get(string $name): mixed`](method-__get.md)
- [`cleanStr($str): string`](method-cleanstr.md)
- [`save(string $str, array $options = array()): bool`](method-save.md)
- [`removeLineFromChunk(string &$line, string &$chunk, int $chunkSize)`](method-removelinefromchunk.md)
- [`size(): int|false`](method-size.md)
- [`filename(): string`](method-filename.md)
- [`pathname(): string|bool`](method-pathname.md)
- [`mtime(): int|false`](method-mtime.md)
- [`get(int $chunkSize = 0, int $chunkNum = 1): array`](method-get.md)
- [`getChunkArray(int $chunkNum = 1, int $chunkSize = 0, bool $reverse = true): array`](method-getchunkarray.md)
- [`getChunk(int $chunkNum = 1, int $chunkSize = 0, bool $reverse = true, bool $clean = true): string`](method-getchunk.md)
- [`getTotalChunks(int $chunkSize = 0): int`](method-gettotalchunks.md)
- [`getTotalLines(): int`](method-gettotallines.md)
- [`getDate(int $dateFrom, int $dateTo = 0, int $pageNum = 1, int $limit = 100): array`](method-getdate.md)
- [`find(int $limit = 100, int $pageNum = 1, array $options = array()): int|array`](method-find.md)
- [`isValidLine($line, array $options, bool &$stopNow): bool`](method-isvalidline.md)
- [`prune($bytes): bool|int`](method-prune.md)
- [`pruneBytes(int $bytes): int|bool`](method-prunebytes.md)
- [`pruneDate(int|string $oldestDate): int`](method-prunedate.md)
- [`delete(): bool`](method-delete.md)
- [`chunkSize(int $chunkSize = 0): int`](method-chunksize.md)
- [`path(): string`](method-path.md)

Constants:
- [`defaultChunkSize`](const-defaultchunksize.md)
- [`debug`](const-debug.md)
