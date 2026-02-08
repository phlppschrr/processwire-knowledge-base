# WireDatabaseBackup::restorePDO()

Source: `wire/core/WireDatabaseBackup.php`

Import a database SQL file using PDO

@param string $filename Filename to restore (must be SQL file exported by this class)

@param array $options See $restoreOptions

@return bool true on success, false on failure. Call the errors() method to retrieve errors.
