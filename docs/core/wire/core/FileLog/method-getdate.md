# $fileLog->getDate($dateFrom, $dateTo = 0, $pageNum = 1, $limit = 100): array

Source: `wire/core/FileLog.php`

Get log lines that lie within a date range

## Usage

~~~~~
// basic usage
$array = $fileLog->getDate($dateFrom);

// usage with all arguments
$array = $fileLog->getDate($dateFrom, $dateTo = 0, $pageNum = 1, $limit = 100);
~~~~~

## Arguments

- `$dateFrom` `int` Starting date (unix timestamp or strtotime compatible string)
- `$dateTo` (optional) `int` Ending date (unix timestamp or strtotime compatible string)
- `$pageNum` (optional) `int` Current pagination number (default=1)
- `$limit` (optional) `int` Items per pagination (default=100), or specify 0 for no limit.

## Return value

- `array`
