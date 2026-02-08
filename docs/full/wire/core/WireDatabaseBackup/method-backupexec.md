# $wireDatabaseBackup->backupExec($file, array $options): string|bool

Source: `wire/core/WireDatabaseBackup.php`

Create a mysql dump file using exec(mysqldump)

## Arguments

- `$file` `string` Path + filename to create
- `$options` `array`

## Return value

string|bool Returns the created file on success or false on error

## Details

- @todo add backupStartFile/backupEndFile support
