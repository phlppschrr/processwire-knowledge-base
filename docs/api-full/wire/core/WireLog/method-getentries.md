# $wireLog->getEntries($name, array $options = array()): array

Source: `wire/core/WireLog.php`

Return given number of entries from end of log file, with each entry as an associative array of components

This is effectively the same as the `getLines()` method except that each entry is an associative
array rather than a single line (string). This method is pagination aware.

## Usage

~~~~~
// basic usage
$array = $wireLog->getEntries($name);

// usage with all arguments
$array = $wireLog->getEntries($name, array $options = array());
~~~~~

## Arguments

- `$name` `string` Name of log file (excluding extension)
- `$options` (optional) `array` Optional options to modify default behavior: - `limit` (integer): Specify number of lines (default=100) - `text` (string): Text to find. - `dateFrom` (int|string): Oldest date to match entries. - `dateTo` (int|string): Newest date to match entries. - `reverse` (bool): Reverse order (default=true) - `pageNum` (int): Pagination number 1 or above (default=0 which means auto-detect)

## Return value

- `array` Returns an array of associative arrays, each with the following components: - `date` (string): ISO-8601 date string - `user` (string): user name or boolean false if unknown - `url` (string): full URL or boolean false if unknown - `text` (string): text of the log entry

## See Also

- [WireLog::getLines()](method-getlines.md)
