# Database::query()

Source: `wire/core/Database.php`

Overrides default mysqli query method so that it also records and times queries.

@param string $sql SQL Query

@param int $resultmode See http://www.php.net/manual/en/mysqli.query.php

@return mixed Returns FALSE on failure.
	For successful SELECT, SHOW, DESCRIBE or EXPLAIN queries mysqli_query() will return a MySQLi_Result object.
	For other successful queries mysqli_query() will return TRUE.

@throws WireDatabaseException
