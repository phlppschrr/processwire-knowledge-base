# $fileLog->getDate($dateFrom, $dateTo = 0, $pageNum = 1, $limit = 100): array

Source: `wire/core/FileLog.php`

Get log lines that lie within a date range

## Arguments

- int $dateFrom Starting date (unix timestamp or strtotime compatible string)
- int $dateTo Ending date (unix timestamp or strtotime compatible string)
- int $pageNum Current pagination number (default=1)
- int $limit Items per pagination (default=100), or specify 0 for no limit.

## Return value

array
