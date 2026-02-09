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
- [`message(string $text, bool|int $flags = 0): Wire|WireLog`](method-message.md) Record an informational or 'success' message in the message log (messages.txt)
- [`error(string $text, int|bool $flags = 0): Wire|WireLog`](method-error.md) Record an error message in the error log (errors.txt)
- [`warning(string $text, int|bool $flags = 0): Wire|WireLog`](method-warning.md) Record a warning message in the warnings log (warnings.txt)
- [`save(string $name, string $text, array $options = array()): bool`](method-___save.md) (hookable) Save text to a named log
- [`getLogs(bool $sortNewest = false): array`](method-getlogs.md) Return array of all logs, sorted by name
- [`getFilename(string $name): string`](method-getfilename.md) Get the full filename (including path) for the given log name
- [`exists(string $name): bool`](method-exists.md) Does given log name exist?
- [`getLines(string $name, array $options = array()): array`](method-getlines.md) Return the given number of entries from the end of log file
- [`getEntries(string $name, array $options = array()): array`](method-getentries.md) Return given number of entries from end of log file, with each entry as an associative array of components
- [`getTotalEntries(string $name): int`](method-gettotalentries.md) Get the total number of entries present in the given log
- [`delete(string $name): bool`](method-delete.md) Delete a log file
- [`deleteAll(bool $throw = false): array`](method-deleteall.md) Delete all log files
- [`prune(string $name, int $days): int`](method-prune.md) Prune log file to contain only entries from last [n] days
- [`pruneAll(int $days): array`](method-pruneall.md) Prune all log files to given number of days
- [`disable(string $name): self`](method-disable.md) Disable the given log name temporarily so that save() calls do not record entries during this request
- [`enable(string $name): self`](method-enable.md) Enable a previously disabled log
- [`path(): string`](method-path.md) Return disk path to log files
