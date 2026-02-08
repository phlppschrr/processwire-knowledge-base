# WireDatabaseBackup::backupExec()

Source: `wire/core/WireDatabaseBackup.php`

Create a mysql dump file using exec(mysqldump)

@param string $file Path + filename to create

@param array $options

@return string|bool Returns the created file on success or false on error

@todo add backupStartFile/backupEndFile support
