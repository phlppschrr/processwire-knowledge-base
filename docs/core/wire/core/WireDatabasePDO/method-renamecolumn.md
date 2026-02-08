# $wireDatabasePDO->renameColumn($table, $oldName, $newName): bool

Source: `wire/core/WireDatabasePDO.php`

Rename a table column without changing type

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDO->renameColumn($table, $oldName, $newName);
~~~~~

## Arguments

- `$table` `string`
- `$oldName` `string`
- `$newName` `string`

## Return value

- `bool`

## Exceptions

- `\PDOException`

## Since

3.0.185
