# Database

Source: `wire/core/Database.php`

Database class provides a layer on top of mysqli

## __construct()

Construct the Database

Since this extends MySQL all the MySQL construct params are kept in tact.
However, you may just supply an object with the following properties if you prefer:
$o->dbUser, $o->dbPass, $o->dbHost, $o->dbName, $config->dbPort, $config->dbSocket (optional).
This would usually be from a ProcessWire Config ($config) API var, but kept as generic object
in case someone wants to use this class elsewhere.

@param string|Config $host Hostname or object with config properties.

@param string $user Username

@param string $pass Password

@param string $db Database name

@param int $port Port

@param string $socket Socket

@throws WireDatabaseException

## query()

Overrides default mysqli query method so that it also records and times queries.

@param string $sql SQL Query

@param int $resultmode See http://www.php.net/manual/en/mysqli.query.php

@return mixed Returns FALSE on failure.
	For successful SELECT, SHOW, DESCRIBE or EXPLAIN queries mysqli_query() will return a MySQLi_Result object.
	For other successful queries mysqli_query() will return TRUE.

@throws WireDatabaseException

## queryLog()

Log a query or return the query log

@param string $sql Omit to instead return the query log

@return array|bool Returns query log array when $sql argument is omitted

## getTables()

Get array of all tables in this database.

@return array

## isOperator()

Is the given string a database comparison operator?

@param string $str 1-2 character opreator to test

@return bool

## setThrowExceptions()

Set whether Exceptions should be thrown on query errors

@param bool $throwExceptions Default is true

## escapeTable()

Sanitize a table name for _a-zA-Z0-9

@param string $table

@return string

## escapeCol()

Sanitize a column name for _a-zA-Z0-9

@param string $col

@return string

## escapeTableCol()

Sanitize a table.column string, where either part is optional

@param string $str

@return string

## escapeStr()

Escape a string value, camelCase alias of escape_string()

@param string $str

@return string

## escapeLike()

Escape a string value, plus escape characters necessary for a MySQL 'LIKE' phrase

@param string $like

@return string
