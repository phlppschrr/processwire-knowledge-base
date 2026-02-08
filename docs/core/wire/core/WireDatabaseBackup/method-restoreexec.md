# WireDatabaseBackup::restoreExec()

Source: `wire/core/WireDatabaseBackup.php`

Import a database SQL file using exec(mysql)

@param string $filename Filename to restore (must be SQL file exported by this class)

@param array $options See $restoreOptions

@return bool True on success, false on failure. Call the errors() method to retrieve errors.
