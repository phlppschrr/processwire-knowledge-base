# WireDatabaseBackup

Source: `wire/core/WireDatabaseBackup.php`

ProcessWire Database Backup and Restore
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

Methods:
- [`__construct(string $path = '')`](method-__construct.md) Construct
- [`setDatabaseConfig(array|Config|object $config): $this`](method-setdatabaseconfig.md) Set the database configuration information
- [`setDatabase(\PDO|WireDatabasePDO $database)`](method-setdatabase.md) Set the PDO database connection
- [`getDatabase(): \PDO`](method-getdatabase.md) Get current database connection, initiating the connection if not yet active
- [`error(string $str = ''): string`](method-error.md) Add an error and return last error
- [`errors(bool $reset = false): array`](method-errors.md) Return all error messages that occurred
- [`note($key, $value)`](method-note.md) Record a note
- [`notes(bool $reset = false): array`](method-notes.md) Get all notes
- [`setPath(string $path): $this`](method-setpath.md) Set path where database files are stored
- [`getPath(): string`](method-getpath.md) Get path where database files are stored
- [`getFiles(bool $getObjects = false): array|\SplFileInfo[]`](method-getfiles.md) Return array of all backup files
- [`getFileInfo(string $filename): array`](method-getfileinfo.md) Get information about a backup file
- [`getAllTables(bool $count = false, bool $cache = true): array`](method-getalltables.md) Get array of all table names
- [`backup(array $options = array()): string`](method-backup.md) Perform a database export/dump
- [`unlink(string $file): bool`](method-unlink.md) Unlink file using PW if available or PHP if not
- [`backupStartFile(string $file, array $options): bool`](method-backupstartfile.md) Start a new backup file, adding our info header to the top
- [`backupEndFile(string|resource $file, array $summary = array(), array $options = array()): bool`](method-backupendfile.md) End a new backup file, adding our footer to the bottom
- [`backupPDO(string $file, array $options = array()): string|bool`](method-backuppdo.md) Create a mysql dump file using PDO
- [`backupExec(string $file, array $options): string|bool`](method-backupexec.md) Create a mysql dump file using exec(mysqldump)
- [`restore(string $filename, array $options = array()): true`](method-restore.md) Restore/import a MySQL database dump file
- [`restorePDO(string $filename, array $options = array()): bool`](method-restorepdo.md) Import a database SQL file using PDO
- [`restoreExec(string $filename, array $options = array()): bool`](method-restoreexec.md) Import a database SQL file using exec(mysql)
- [`restoreUseLine($line): bool`](method-restoreuseline.md) Returns true or false if a line should be used for restore
- [`restoreMerge(string $filename1, string $filename2, array $options): bool`](method-restoremerge.md) Restore from 2 SQL files while resolving table differences (think of it as array_merge for a DB restore)
- [`dropAllTables(): int`](method-dropalltables.md) Drop all tables from database
- [`findStatements(string $filename, string $regex, bool $multi = true): array`](method-findstatements.md) Returns array of all create table statements, indexed by table name
- [`executeQuery(string|\PDOStatement $query, bool|array $options = array()): bool`](method-executequery.md) Execute an SQL query, either a string or PDOStatement
- [`sanitizePath($path): string`](method-sanitizepath.md) For path: Normalizes slashes and ensures it ends with a slash
- [`sanitizeFilename($filename): string`](method-sanitizefilename.md) For filename: Normalizes slashes and ensures it starts with a path
- [`supportsExec(array $options = array()): bool`](method-supportsexec.md) Determine if exec is available for the given command
