# $fileLog->pruneBytes($bytes): int|bool

Source: `wire/core/FileLog.php`

Prune log file to specified number of bytes (from the end)

## Arguments

- `$bytes` `int`

## Return value

int|bool positive integer on success, 0 if no prune necessary, or boolean false on failure.
