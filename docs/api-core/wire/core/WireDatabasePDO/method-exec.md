# $wireDatabasePDO->exec($statement, $note = ''): bool|int

Source: `wire/core/WireDatabasePDO.php`

Execute an SQL statement string

If given a PDOStatement, this method behaves the same as the execute() method.

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDO->exec($statement);

// usage with all arguments
$bool = $wireDatabasePDO->exec($statement, $note = '');
~~~~~

## Arguments

- `$statement` `string|\PDOStatement`
- `$note` (optional) `string`

## Return value

- `bool|int`

## Exceptions

- `\PDOException`

## Details

- @link http://php.net/manual/en/pdo.exec.php
