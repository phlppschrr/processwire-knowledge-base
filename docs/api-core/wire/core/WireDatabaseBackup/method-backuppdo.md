# $wireDatabaseBackup->backupPDO($file, array $options = array()): string|bool

Source: `wire/core/WireDatabaseBackup.php`

Create a mysql dump file using PDO

## Usage

~~~~~
// basic usage
$string = $wireDatabaseBackup->backupPDO($file);

// usage with all arguments
$string = $wireDatabaseBackup->backupPDO($file, array $options = array());
~~~~~

## Arguments

- `$file` `string` Path + filename to create
- `$options` (optional) `array`

## Return value

- `string|bool` Returns the created file on success or false on error
