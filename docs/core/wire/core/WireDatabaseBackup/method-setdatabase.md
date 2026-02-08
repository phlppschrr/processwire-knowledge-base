# $wireDatabaseBackup->setDatabase($database)

Source: `wire/core/WireDatabaseBackup.php`

Set the PDO database connection

## Usage

~~~~~
// basic usage
$result = $wireDatabaseBackup->setDatabase($database);
~~~~~

## Arguments

- `$database` `\PDO|WireDatabasePDO`

## Exceptions

- `\PDOException` on invalid connection
