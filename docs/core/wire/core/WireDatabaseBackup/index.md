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
- [`__construct(string $path = '')`](method-__construct.md)
- [`setDatabaseConfig(array|Config|object $config): $this`](method-setdatabaseconfig.md)
- [`setDatabase(\PDO|WireDatabasePDO $database)`](method-setdatabase.md)
- [`getDatabase(): \PDO`](method-getdatabase.md)
- [`error(string $str = ''): string`](method-error.md)
- [`errors(bool $reset = false): array`](method-errors.md)
- [`note($key, $value)`](method-note.md)
- [`notes(bool $reset = false): array`](method-notes.md)
- [`setPath(string $path): $this`](method-setpath.md)
- [`getPath(): string`](method-getpath.md)
- [`getFiles(bool $getObjects = false): array|\SplFileInfo[]`](method-getfiles.md)
- [`getFileInfo(string $filename): array`](method-getfileinfo.md)
- [`getAllTables(bool $count = false, bool $cache = true): array`](method-getalltables.md)
- [`backup(array $options = array()): string`](method-backup.md)
- [`unlink(string $file): bool`](method-unlink.md)
- [`backupStartFile(string $file, array $options): bool`](method-backupstartfile.md)
- [`backupEndFile(string|resource $file, array $summary = array(), array $options = array()): bool`](method-backupendfile.md)
- [`backupPDO(string $file, array $options = array()): string|bool`](method-backuppdo.md)
- [`backupExec(string $file, array $options): string|bool`](method-backupexec.md)
- [`restore(string $filename, array $options = array()): true`](method-restore.md)
- [`restorePDO(string $filename, array $options = array()): bool`](method-restorepdo.md)
- [`restoreExec(string $filename, array $options = array()): bool`](method-restoreexec.md)
- [`restoreUseLine($line): bool`](method-restoreuseline.md)
- [`restoreMerge(string $filename1, string $filename2, array $options): bool`](method-restoremerge.md)
- [`dropAllTables(): int`](method-dropalltables.md)
- [`findStatements(string $filename, string $regex, bool $multi = true): array`](method-findstatements.md)
- [`executeQuery(string|\PDOStatement $query, bool|array $options = array()): bool`](method-executequery.md)
- [`sanitizePath($path): string`](method-sanitizepath.md)
- [`sanitizeFilename($filename): string`](method-sanitizefilename.md)
- [`supportsExec(array $options = array()): bool`](method-supportsexec.md)
