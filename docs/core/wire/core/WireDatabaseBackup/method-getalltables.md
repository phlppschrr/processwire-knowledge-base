# $wireDatabaseBackup->getAllTables($count = false, $cache = true): array

Source: `wire/core/WireDatabaseBackup.php`

Get array of all table names

## Usage

~~~~~
// basic usage
$array = $wireDatabaseBackup->getAllTables();

// usage with all arguments
$array = $wireDatabaseBackup->getAllTables($count = false, $cache = true);
~~~~~

## Arguments

- `$count` (optional) `bool` If true, returns array indexed by name with count of records as value
- `$cache` (optional) `bool` Allow use of cache?

## Return value

- `array`
