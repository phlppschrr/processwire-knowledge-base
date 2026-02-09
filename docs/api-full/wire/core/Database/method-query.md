# $database->query($sql, $resultmode = MYSQLI_STORE_RESULT): mixed

Source: `wire/core/Database.php`

Overrides default mysqli query method so that it also records and times queries.

## Usage

~~~~~
// basic usage
$result = $database->query($sql);

// usage with all arguments
$result = $database->query($sql, $resultmode = MYSQLI_STORE_RESULT);
~~~~~

## Arguments

- `$sql` `string` SQL Query
- `$resultmode` (optional) `int` See http://www.php.net/manual/en/mysqli.query.php

## Return value

- `mixed` Returns FALSE on failure. For successful SELECT, SHOW, DESCRIBE or EXPLAIN queries mysqli_query() will return a MySQLi_Result object. For other successful queries mysqli_query() will return TRUE.

## Exceptions

- `WireDatabaseException`
