# $wireDatabaseBackup->backupExec($file, array $options): string|bool

Source: `wire/core/WireDatabaseBackup.php`

Create a mysql dump file using exec(mysqldump)

## Usage

~~~~~
// basic usage
$string = $wireDatabaseBackup->backupExec($file, $options);

// usage with all arguments
$string = $wireDatabaseBackup->backupExec($file, array $options);
~~~~~

## Arguments

- `$file` `string` Path + filename to create
- `$options` `array`

## Return value

- `string|bool` Returns the created file on success or false on error

## Details

- @todo add backupStartFile/backupEndFile support
