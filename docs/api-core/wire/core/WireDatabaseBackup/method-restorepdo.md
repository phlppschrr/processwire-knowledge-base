# $wireDatabaseBackup->restorePDO($filename, array $options = array()): bool

Source: `wire/core/WireDatabaseBackup.php`

Import a database SQL file using PDO

## Usage

~~~~~
// basic usage
$bool = $wireDatabaseBackup->restorePDO($filename);

// usage with all arguments
$bool = $wireDatabaseBackup->restorePDO($filename, array $options = array());
~~~~~

## Arguments

- `$filename` `string` Filename to restore (must be SQL file exported by this class)
- `$options` (optional) `array` See $restoreOptions

## Return value

- `bool` true on success, false on failure. Call the errors() method to retrieve errors.
