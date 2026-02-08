# $fileLog->pruneDate($oldestDate): int

Source: `wire/core/FileLog.php`

Prune log file to contain only entries newer than $oldestDate

## Usage

~~~~~
// basic usage
$int = $fileLog->pruneDate($oldestDate);
~~~~~

## Arguments

- `$oldestDate` `int|string`

## Return value

- `int` Number of lines written
