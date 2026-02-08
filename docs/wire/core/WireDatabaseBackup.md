# WireDatabaseBackup

Source: `wire/core/WireDatabaseBackup.php`

ProcessWire Database Backup and Restore
It’s not typically necessary to call these initialization methods unless doing manual initialization.
$backup
$backup = $database->backups();
This class intentionally does not have any external dependencies (other than PDO)
so that it can be included by outside tools for restoring/exporting, with the main
example of that being the ProcessWire installer.

The recommended way to access these backup methods is via the `$database` API variable
method `$database->backups()`, which returns a `WireDatabaseBackup` instance, however
you can also initialize the class manually if you prefer, like this:
~~~~~
// determine where backups will go (should NOT be web accessible)
$backupPath = $config->paths->assets . 'backups/';

// create a new WireDatabaseBackup instance
$backup = new WireDatabaseBackup($backupPath);

// Option 1: set the already-connected DB connection
$backup->setDatabase($this->database);

// Option 2: OR provide a Config object that contains the DB connection info
$backup->setDatabaseConfig($this->config);

~~~~~
### Backup the database
~~~~~
$file = $backup->backup();
if($file) {
  echo "Backed up to: $file";
} else {
  echo "Backup failed: " . implode("<br>", $backup->errors());
}
~~~~~

### Restore a database
~~~~~
$success = $backup->restore($file);
if($success) {
  echo "Restored database from file: $file";
} else {
  echo "Restore failed: " . implode("<br>", $backup->errors());
}
~~~~~

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

## __construct()

Construct

You should follow-up the construct call with one or both of the following:

	- $backups->setDatabase(PDO|WireDatabasePDO);
	- $backups->setDatabaseConfig(array|object);


@param string $path Path where database files are stored

@throws \Exception

## setDatabaseConfig()

Set the database configuration information


@param array|Config|object $config Containing these properties:
 - dbUser
 - dbHost
 - dbPort
 - dbName
	- dbPass
 - dbPath (optional)
 - dbCharset (optional)

@return $this

@throws \Exception if missing required config settings

## setDatabase()

Set the PDO database connection


@param \PDO|WireDatabasePDO $database

@throws \PDOException on invalid connection

## getDatabase()

Get current database connection, initiating the connection if not yet active


@return \PDO

@throws \Exception

## error()

Add an error and return last error


@param string $str If omitted, no error is added

@return string

## errors()

Return all error messages that occurred


@param bool $reset Specify true to clear out existing errors or omit just to return error messages

@return array

## note()

Record a note


@param $key

@param $value

## notes()

Get all notes


@param bool $reset

@return array

## setPath()

Set path where database files are stored


@param string $path

@return $this

@throws \Exception if path has a problem

## getPath()

Get path where database files are stored


@return string

## getFiles()

Return array of all backup files

To get additional info on any of them, call getFileInfo($basename) method


@param bool $getObjects Get SplFileInfo objects rather than basenames? (3.0.214+)

@return array|\SplFileInfo[] Array of strings (basenames), or array of SplFileInfo objects (when requested)

## getFileInfo()

Get information about a backup file


@param string $filename

@return array Returns associative array of information on success, empty array on failure

## getAllTables()

Get array of all table names


@param bool $count If true, returns array indexed by name with count of records as value

@param bool $cache Allow use of cache?

@return array

## backup()

Perform a database export/dump


@param array $options Options to modify default behavior:
- `filename` (string): filename for backup: default is to make a dated filename, but this can also be used (basename only, no path)
- `description` (string): optional description of this backup
- `tables` (array): if specified, export will only include these tables
- `user` (string): username to associate with the backup file (string), optional
- `excludeTables` (array): exclude creating or inserting into these tables
- `excludeCreateTables` (array): exclude creating these tables, but still export data
- `excludeExportTables` (array): exclude exporting data, but still create tables
- `whereSQL` (array): SQL conditions for export of individual tables [table => [SQL conditions]]. The `table` portion (index) may also be a full PCRE regexp, must start with `/` to be recognized as regex.
- `maxSeconds` (int): max number of seconds allowed for execution (default=1200)
- `allowDrop` (bool): use DROP TABLES statements before CREATE TABLE statements? (default=true)
- `allowUpdate` (bool): use UPDATE ON DUPLICATE KEY so that INSERT statements can UPDATE when rows already present (all tables). (default=false)
- `allowUpdateTables` (array): table names that will use UPDATE ON DUPLICATE KEY (does NOT require allowUpdate=true)
- `findReplace` (array): find and replace in row data during backup. Example: ['databass' => 'database']
- `findReplaceCreateTable` (array): find and replace in create table statements
   Example: ['DEFAULT CHARSET=latin1;' => 'DEFAULT CHARSET=utf8;']
- `extraSQL` (array): additional SQL queries to append at the bottom. Example: ['UPDATE pages SET created=NOW()']

@return string Full path and filename of database export file, or false on failure.

@throws \Exception on fatal error

@see WireDatabaseBackup::restore()

## unlink()

Unlink file using PW if available or PHP if not

@param string $file

@return bool

@throws WireException

## backupStartFile()

Start a new backup file, adding our info header to the top

@param string $file

@param array $options

@return bool

## backupEndFile()

End a new backup file, adding our footer to the bottom

@param string|resource $file

@param array $summary

@param array $options

@return bool

## backupPDO()

Create a mysql dump file using PDO

@param string $file Path + filename to create

@param array $options

@return string|bool Returns the created file on success or false on error

## backupExec()

Create a mysql dump file using exec(mysqldump)

@param string $file Path + filename to create

@param array $options

@return string|bool Returns the created file on success or false on error

@todo add backupStartFile/backupEndFile support

## restore()

Restore/import a MySQL database dump file

This method is designed to restore dump files created by the backup() method of this
class, however it *may* also work with dump files created from other sources like
mysqldump or PhpMyAdmin.


@param string $filename Filename to restore, optionally including path (if no path, then path set to construct is assumed)

@param array $options Options to modify default behavior:
- `tables` (array): table names to restore (empty=all)
- `allowDrop` (bool): allow DROP TABLE statements (default=true)
- `dropAll` (bool): DROP ALL tables before restore? The allowDrop optional must also be true. (default=false)
- `haltOnError` (bool): halt execution when an error occurs? (default=false)
- `maxSeconds` (int): max number of seconds allowed for execution (default=1200)
- `findReplace` (array): find and replace in row data. Example: ['databass' => 'database']
- `findReplaceCreateTable` (array): find and replace in create table statements.
   Example: ['DEFAULT CHARSET=utf8;' => 'DEFAULT CHARSET=utf8mb4;']

@return true on success, false on failure. Call the errors() method to retrieve errors.

@throws \Exception on fatal error

@see WireDatabaseBackup::backup()

## restorePDO()

Import a database SQL file using PDO

@param string $filename Filename to restore (must be SQL file exported by this class)

@param array $options See $restoreOptions

@return bool true on success, false on failure. Call the errors() method to retrieve errors.

## restoreExec()

Import a database SQL file using exec(mysql)

@param string $filename Filename to restore (must be SQL file exported by this class)

@param array $options See $restoreOptions

@return bool True on success, false on failure. Call the errors() method to retrieve errors.

## restoreUseLine()

Returns true or false if a line should be used for restore

@param $line

@return bool

## restoreMerge()

Restore from 2 SQL files while resolving table differences (think of it as array_merge for a DB restore)

The CREATE TABLE and INSERT statements in filename2 take precedence of those in filename1.
INSERT statements from both will be executed, with filename2 INSERTs updating those of filename1.
CREATE TABLE statements in filename1 won't be executed if they also exist in filename2.

This method assumes both files follow the SQL dump format created by this class.


@param string $filename1 Original filename

@param string $filename2 Filename that may have statements that will update/override those in filename1

@param array $options

@return bool True on success, false on fail.

@throws \Exception|WireException if $options['haltOnErrors'] == true.

## dropAllTables()

Drop all tables from database

@return int Quantity of tables dropped

@throws \Exception

@since 3.0.130

## findStatements()

Returns array of all create table statements, indexed by table name

@param string $filename to extract all CREATE TABLE statements from

@param string $regex Regex (PCRE) to match for statement to be returned, must stuff table name into first match

@param bool $multi Whether there can be multiple matches per table

@return array of statements, indexed by table name. If $multi is true, it will be array of arrays.

@throws \Exception if unable to open specified file

## executeQuery()

Execute an SQL query, either a string or PDOStatement

@param string|\PDOStatement $query

@param bool|array $options May be boolean (for haltOnError), or array containing the property (i.e. $options array)
 - `haltOnError` (bool): Halt execution when error occurs? (default=false)

@return bool Query result

@throws \Exception if haltOnError, otherwise it populates $this->errors

## sanitizePath()

For path: Normalizes slashes and ensures it ends with a slash

@param $path

@return string

## sanitizeFilename()

For filename: Normalizes slashes and ensures it starts with a path

@param $filename

@return string

@throws \Exception if path has not yet been set

## supportsExec()

Determine if exec is available for the given command

Note that WireDatabaseBackup does not currently use exec() mode so this is here for future use.

@param array $options

@return bool

@throws \Exception on unknown exec type
