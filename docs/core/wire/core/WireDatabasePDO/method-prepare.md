# WireDatabasePDO::prepare()

Source: `wire/core/WireDatabasePDO.php`

Prepare an SQL statement for accepting bound parameters


@param string $statement

@param array|string|bool $driver_options Optionally specify one of the following:
 - Boolean true for WireDatabasePDOStatement rather than PDOStatement (also assumed when debug mode is on) 3.0.162+
 - Driver options array
 - or you may specify the $note argument here

@param string $note Debug notes to save with query in debug mode

@return \PDOStatement|WireDatabasePDOStatement

@link http://php.net/manual/en/pdo.prepare.php
