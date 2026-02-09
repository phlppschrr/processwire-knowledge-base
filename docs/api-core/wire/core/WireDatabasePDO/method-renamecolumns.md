# $wireDatabasePDO->renameColumns($table, array $columns): int

Source: `wire/core/WireDatabasePDO.php`

Rename table columns without changing type

## Usage

~~~~~
// basic usage
$int = $wireDatabasePDO->renameColumns($table, $columns);

// usage with all arguments
$int = $wireDatabasePDO->renameColumns($table, array $columns);
~~~~~

## Arguments

- `$table` `string`
- `$columns` `array` Associative array with one or more of `[ 'old_name' => 'new_name' ]`

## Return value

- `int` Number of columns renamed

## Exceptions

- `\PDOException`

## Since

3.0.185
