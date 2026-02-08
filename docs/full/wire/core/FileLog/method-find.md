# $fileLog->find($limit = 100, $pageNum = 1, array $options = array()): int|array

Source: `wire/core/FileLog.php`

Return lines from the end of the log file, with various options

## Arguments

- int $limit Number of items to return (per pagination), or 0 for no limit.
- int $pageNum Current pagination (default=1)
- array $options - text (string): Return only lines containing the given string of text - reverse (bool): True=find from end of file, false=find from beginning (default=true) - toFile (string): Send results to the given basename (default=none) - dateFrom (unix timestamp): Return only lines newer than the given date (default=oldest) - dateTo (unix timestamp): Return only lines older than the given date  (default=now) Note: dateFrom and dateTo may be combined to return a range.

## Return value

int|array of strings (associative), each indexed by string containing slash separated numeric values of: "current/total/start/end/total" which is useful with pagination. If the 'toFile' option is used, then return value is instead an integer qty of lines written.

## Throws

- \Exception on fatal error
