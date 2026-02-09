# WireLog

Source: `wire/core/WireLog.php`

Inherits: `Wire`


Groups:
Group: [other](group-other.md)

ProcessWire Log

WireLog represents the ProcessWire $log API variable.
It is an API-friendly interface to the FileLog class.

Enables creation of logs, logging of events, and management of logs.



@todo option to disable logs by name

Methods:
- [`message(string $text, bool|int $flags = 0): Wire|WireLog`](method-message.md)
- [`error(string $text, int|bool $flags = 0): Wire|WireLog`](method-error.md)
- [`warning(string $text, int|bool $flags = 0): Wire|WireLog`](method-warning.md)
- [`save(string $name, string $text, array $options = array()): bool`](method-___save.md) (hookable)
- [`getLogs(bool $sortNewest = false): array`](method-getlogs.md)
- [`getFilename(string $name): string`](method-getfilename.md)
- [`exists(string $name): bool`](method-exists.md)
- [`getLines(string $name, array $options = array()): array`](method-getlines.md)
- [`getEntries(string $name, array $options = array()): array`](method-getentries.md)
- [`getTotalEntries(string $name): int`](method-gettotalentries.md)
- [`delete(string $name): bool`](method-delete.md)
- [`deleteAll(bool $throw = false): array`](method-deleteall.md)
- [`prune(string $name, int $days): int`](method-prune.md)
- [`pruneAll(int $days): array`](method-pruneall.md)
- [`disable(string $name): self`](method-disable.md)
- [`enable(string $name): self`](method-enable.md)
- [`path(): string`](method-path.md)
