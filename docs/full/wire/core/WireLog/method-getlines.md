# WireLog::getLines()

Source: `wire/core/WireLog.php`

Return the given number of entries from the end of log file

This method is pagination aware.


@param string $name Name of log

@param array $options Specify any of the following:
	- `limit` (integer): Specify number of lines (default=100)
	- `text` (string): Text to find.
	- `dateFrom` (int|string): Oldest date to match entries.
	- `dateTo` (int|string): Newest date to match entries.
	- `reverse` (bool): Reverse order (default=true)
	- `pageNum` (int): Pagination number 1 or above (default=0 which means auto-detect)

@return array

@see WireLog::getEntries()
