# $wireLog->getLines($name, array $options = array()): array

Source: `wire/core/WireLog.php`

Return the given number of entries from the end of log file

This method is pagination aware.

## Usage

~~~~~
// basic usage
$array = $wireLog->getLines($name);

// usage with all arguments
$array = $wireLog->getLines($name, array $options = array());
~~~~~

## Arguments

- `$name` `string` Name of log
- `$options` (optional) `array` Specify any of the following: - `limit` (integer): Specify number of lines (default=100) - `text` (string): Text to find. - `dateFrom` (int|string): Oldest date to match entries. - `dateTo` (int|string): Newest date to match entries. - `reverse` (bool): Reverse order (default=true) - `pageNum` (int): Pagination number 1 or above (default=0 which means auto-detect)

## Return value

- `array`

## See Also

- [WireLog::getEntries()](method-getentries.md)
