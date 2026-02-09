# $wireDatabasePDO->supportsTransaction($table = ''): bool

Source: `wire/core/WireDatabasePDO.php`

Are transactions available with current DB engine (or table)?

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDO->supportsTransaction();

// usage with all arguments
$bool = $wireDatabasePDO->supportsTransaction($table = '');
~~~~~

## Arguments

- `$table` (optional) `string` Optionally specify a table to specifically check to that table

## Return value

- `bool`
