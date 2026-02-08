# $wireDatabasePDO->escapeTable($table): string

Source: `wire/core/WireDatabasePDO.php`

Sanitize a table name for _a-zA-Z0-9

## Usage

~~~~~
// basic usage
$string = $wireDatabasePDO->escapeTable($table);
~~~~~

## Arguments

- `$table` `string` String containing table name

## Return value

- `string` Sanitized table name
