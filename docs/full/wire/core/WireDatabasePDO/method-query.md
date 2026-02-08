# $wireDatabasePDO->query($statement, $note = ''): \PDOStatement

Source: `wire/core/WireDatabasePDO.php`

Executes an SQL statement, returning a result set as a PDOStatement object

## Usage

~~~~~
// basic usage
$result = $wireDatabasePDO->query($statement);

// usage with all arguments
$result = $wireDatabasePDO->query($statement, $note = '');
~~~~~

## Arguments

- `$statement` `string`
- `$note` (optional) `string`

## Return value

- `\PDOStatement`

## Details

- @link http://php.net/manual/en/pdo.query.php
