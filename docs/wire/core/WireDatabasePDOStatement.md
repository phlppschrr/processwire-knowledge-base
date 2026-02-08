# WireDatabasePDOStatement

Source: `wire/core/WireDatabasePDOStatement.php`

ProcessWire PDO Statement

Serves as a wrapper to PHP’s PDOStatement class, purely for debugging purposes.
When ProcessWire is not in debug mode, this class is not used at present.

The primary thing this class does is log queries with the bind parameters
populated into the SQL query string, purely for readability purposes. These
populated queries are not ever used for actual database queries, just for logs.

Note that this class only tracks bindValue() and does not track bindParam().

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

## __construct()

Construct

PDO requires the PDOStatement constructor to be protected for some reason

@param WireDatabasePDO $database

## setDebugNote()

Set debug note

@param string $note

## setDebugParam()

Set a named debug parameter

@param string $parameter

@param int|string|null $value

@param int|null $data_type \PDO::PARAM_* type

## bindValue()

Bind a value for this statement

@param string|int $parameter

@param mixed $value

@param int $data_type

@return bool

## execute()

Execute prepared statement

@param array|null $input_parameters

@return bool

@throws \PDOException

## executeDebug()

Execute prepared statement when in debug mode only

@param array|null $input_parameters

@return bool

@throws \PDOException
