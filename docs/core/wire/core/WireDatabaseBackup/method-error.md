# $wireDatabaseBackup->error($str = ''): string

Source: `wire/core/WireDatabaseBackup.php`

Add an error and return last error

## Usage

~~~~~
// basic usage
$string = $wireDatabaseBackup->error();

// usage with all arguments
$string = $wireDatabaseBackup->error($str = '');
~~~~~

## Arguments

- `$str` (optional) `string` If omitted, no error is added

## Return value

- `string`
