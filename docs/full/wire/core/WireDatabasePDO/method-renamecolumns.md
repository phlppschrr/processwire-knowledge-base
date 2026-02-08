# $wireDatabasePDO->renameColumns($table, array $columns): int

Source: `wire/core/WireDatabasePDO.php`

Rename table columns without changing type

## Arguments

- string $table
- array $columns Associative array with one or more of `[ 'old_name' => 'new_name' ]`

## Return value

int Number of columns renamed

## Throws

- \PDOException

## Meta

- @since 3.0.185
