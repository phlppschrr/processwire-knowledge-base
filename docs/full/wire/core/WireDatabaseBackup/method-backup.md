# $wireDatabaseBackup->backup(array $options = array()): string

Source: `wire/core/WireDatabaseBackup.php`

Perform a database export/dump

## Arguments

- array $options Options to modify default behavior: - `filename` (string): filename for backup: default is to make a dated filename, but this can also be used (basename only, no path) - `description` (string): optional description of this backup - `tables` (array): if specified, export will only include these tables - `user` (string): username to associate with the backup file (string), optional - `excludeTables` (array): exclude creating or inserting into these tables - `excludeCreateTables` (array): exclude creating these tables, but still export data - `excludeExportTables` (array): exclude exporting data, but still create tables - `whereSQL` (array): SQL conditions for export of individual tables [table => [SQL conditions]]. The `table` portion (index) may also be a full PCRE regexp, must start with `/` to be recognized as regex. - `maxSeconds` (int): max number of seconds allowed for execution (default=1200) - `allowDrop` (bool): use DROP TABLES statements before CREATE TABLE statements? (default=true) - `allowUpdate` (bool): use UPDATE ON DUPLICATE KEY so that INSERT statements can UPDATE when rows already present (all tables). (default=false) - `allowUpdateTables` (array): table names that will use UPDATE ON DUPLICATE KEY (does NOT require allowUpdate=true) - `findReplace` (array): find and replace in row data during backup. Example: ['databass' => 'database'] - `findReplaceCreateTable` (array): find and replace in create table statements Example: ['DEFAULT CHARSET=latin1;' => 'DEFAULT CHARSET=utf8;'] - `extraSQL` (array): additional SQL queries to append at the bottom. Example: ['UPDATE pages SET created=NOW()']

## Return value

string Full path and filename of database export file, or false on failure.

## Throws

- \Exception on fatal error

## See also

- [WireDatabaseBackup::restore()](method-restore.md)
