# $databaseQuery->copyTo(DatabaseQuery $query, array $methods = array()): int

Source: `wire/core/DatabaseQuery.php`

Copy queries from this DatabaseQuery to another DatabaseQuery

If you want to copy bind values you should also call copyBindValuesTo($query) afterwards.

## Arguments

- `$query` `DatabaseQuery` Query to copy data to
- `$methods` (optional) `array` Optionally specify the names of methods to copy, otherwise all are copied

## Return value

int Total items copied

## Since

3.0.157
