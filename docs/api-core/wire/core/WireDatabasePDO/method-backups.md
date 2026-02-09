# $wireDatabasePDO->backups(): WireDatabaseBackup

Source: `wire/core/WireDatabasePDO.php`

Retrieve new instance of WireDatabaseBackups ready to use with this connection

See `WireDatabaseBackup` class for usage.

## Usage

~~~~~
// basic usage
$wireDatabaseBackup = $wireDatabasePDO->backups();
~~~~~

## Return value

- `WireDatabaseBackup`

## Exceptions

- `WireException|\Exception` on fatal error

## See Also

- [WireDatabaseBackup::backup()](../WireDatabaseBackup/method-backup.md)
- [WireDatabaseBackup::restore()](../WireDatabaseBackup/method-restore.md)
