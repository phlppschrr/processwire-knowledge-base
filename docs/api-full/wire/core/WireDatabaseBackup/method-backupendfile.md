# $wireDatabaseBackup->backupEndFile($file, array $summary = array(), array $options = array()): bool

Source: `wire/core/WireDatabaseBackup.php`

End a new backup file, adding our footer to the bottom

## Usage

~~~~~
// basic usage
$bool = $wireDatabaseBackup->backupEndFile($file);

// usage with all arguments
$bool = $wireDatabaseBackup->backupEndFile($file, array $summary = array(), array $options = array());
~~~~~

## Arguments

- `$file` `string|resource`
- `$summary` (optional) `array`
- `$options` (optional) `array`

## Return value

- `bool`
