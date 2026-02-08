# $wireDatabaseBackup->restore($filename, array $options = array()): true

Source: `wire/core/WireDatabaseBackup.php`

Restore/import a MySQL database dump file

This method is designed to restore dump files created by the backup() method of this
class, however it *may* also work with dump files created from other sources like
mysqldump or PhpMyAdmin.

## Usage

~~~~~
// basic usage
$result = $wireDatabaseBackup->restore($filename);

// usage with all arguments
$result = $wireDatabaseBackup->restore($filename, array $options = array());
~~~~~

## Arguments

- `$filename` `string` Filename to restore, optionally including path (if no path, then path set to construct is assumed)
- `$options` (optional) `array` Options to modify default behavior: - `tables` (array): table names to restore (empty=all) - `allowDrop` (bool): allow DROP TABLE statements (default=true) - `dropAll` (bool): DROP ALL tables before restore? The allowDrop optional must also be true. (default=false) - `haltOnError` (bool): halt execution when an error occurs? (default=false) - `maxSeconds` (int): max number of seconds allowed for execution (default=1200) - `findReplace` (array): find and replace in row data. Example: ['databass' => 'database'] - `findReplaceCreateTable` (array): find and replace in create table statements. Example: ['DEFAULT CHARSET=utf8;' => 'DEFAULT CHARSET=utf8mb4;']

## Return value

- `true` on success, false on failure. Call the errors() method to retrieve errors.

## Exceptions

- `\Exception` on fatal error

## See Also

- [WireDatabaseBackup::backup()](method-backup.md)
