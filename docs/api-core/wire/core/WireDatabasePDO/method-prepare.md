# $wireDatabasePDO->prepare($statement, $driver_options = array(), $note = ''): \PDOStatement|WireDatabasePDOStatement

Source: `wire/core/WireDatabasePDO.php`

Prepare an SQL statement for accepting bound parameters

## Usage

~~~~~
// basic usage
$result = $wireDatabasePDO->prepare($statement);

// usage with all arguments
$result = $wireDatabasePDO->prepare($statement, $driver_options = array(), $note = '');
~~~~~

## Arguments

- `$statement` `string`
- `$driver_options` (optional) `array|string|bool` Optionally specify one of the following: - Boolean true for WireDatabasePDOStatement rather than PDOStatement (also assumed when debug mode is on) 3.0.162+ - Driver options array - or you may specify the $note argument here
- `$note` (optional) `string` Debug notes to save with query in debug mode

## Return value

- `\PDOStatement|WireDatabasePDOStatement`

## Details

- @link http://php.net/manual/en/pdo.prepare.php
