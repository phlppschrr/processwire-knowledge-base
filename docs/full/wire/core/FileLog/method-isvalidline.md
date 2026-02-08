# $fileLog->isValidLine($line, array $options, &$stopNow): bool

Source: `wire/core/FileLog.php`

Returns whether the given log line is valid to be considered a log entry

## Arguments

- $line
- array $options
- bool $stopNow Populates this with true when it can determine no more lines are necessary.

## Return value

bool Returns boolean true if valid, false if not.
