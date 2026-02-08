# FileLog::getDate()

Source: `wire/core/FileLog.php`

Get log lines that lie within a date range

@param int $dateFrom Starting date (unix timestamp or strtotime compatible string)

@param int $dateTo Ending date (unix timestamp or strtotime compatible string)

@param int $pageNum Current pagination number (default=1)

@param int $limit Items per pagination (default=100), or specify 0 for no limit.

@return array
