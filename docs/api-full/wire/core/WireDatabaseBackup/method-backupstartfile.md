# $wireDatabaseBackup->backupStartFile($file, array $options): bool

Source: `wire/core/WireDatabaseBackup.php`

Start a new backup file, adding our info header to the top

## Usage

~~~~~
// basic usage
$bool = $wireDatabaseBackup->backupStartFile($file, $options);

// usage with all arguments
$bool = $wireDatabaseBackup->backupStartFile($file, array $options);
~~~~~

## Arguments

- `$file` `string`
- `$options` `array`

## Return value

- `bool`
