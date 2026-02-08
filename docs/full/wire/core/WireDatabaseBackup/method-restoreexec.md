# $wireDatabaseBackup->restoreExec($filename, array $options = array()): bool

Source: `wire/core/WireDatabaseBackup.php`

Import a database SQL file using exec(mysql)

## Arguments

- string $filename Filename to restore (must be SQL file exported by this class)
- array $options See $restoreOptions

## Return value

bool True on success, false on failure. Call the errors() method to retrieve errors.
