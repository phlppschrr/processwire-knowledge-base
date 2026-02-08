# $wireDatabasePDO->exec($statement, $note = ''): bool|int

Source: `wire/core/WireDatabasePDO.php`

Execute an SQL statement string

If given a PDOStatement, this method behaves the same as the execute() method.

## Arguments

- `$statement` `string|\PDOStatement`
- `$note` (optional) `string`

## Return value

bool|int

## Throws

- \PDOException

## Details

- @link http://php.net/manual/en/pdo.exec.php
