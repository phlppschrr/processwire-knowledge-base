# $wireLog->getLogs($sortNewest = false): array

Source: `wire/core/WireLog.php`

Return array of all logs, sorted by name

Each item in returned array is an associative array that includes the following:

	- `name` (string): Name of log file, excluding extension.
	- `file` (string): Full path and filename of log file.
	- `size` (int): Size in bytes
	- `modified` (int): Last modified date (unix timestamp)

## Arguments

- bool $sortNewest Sort by newest to oldest rather than by name? (default=false) Added 3.0.143

## Return value

array Indexed by log name
