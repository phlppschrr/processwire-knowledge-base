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
Method: [__construct()](method-__construct.md)
Method: [setDatabaseConfig()](method-setdatabaseconfig.md)
Method: [setDatabase()](method-setdatabase.md)
Method: [getDatabase()](method-getdatabase.md)
Method: [error()](method-error.md)
Method: [errors()](method-errors.md)
Method: [note()](method-note.md)
Method: [notes()](method-notes.md)
Method: [setPath()](method-setpath.md)
Method: [getPath()](method-getpath.md)
Method: [getFiles()](method-getfiles.md)
Method: [getFileInfo()](method-getfileinfo.md)
Method: [getAllTables()](method-getalltables.md)
Method: [backup()](method-backup.md)
Method: [unlink()](method-unlink.md)
Method: [backupStartFile()](method-backupstartfile.md)
Method: [backupEndFile()](method-backupendfile.md)
Method: [backupPDO()](method-backuppdo.md)
Method: [backupExec()](method-backupexec.md)
Method: [restore()](method-restore.md)
Method: [restorePDO()](method-restorepdo.md)
Method: [restoreExec()](method-restoreexec.md)
Method: [restoreUseLine()](method-restoreuseline.md)
Method: [restoreMerge()](method-restoremerge.md)
Method: [dropAllTables()](method-dropalltables.md)
Method: [findStatements()](method-findstatements.md)
Method: [executeQuery()](method-executequery.md)
Method: [sanitizePath()](method-sanitizepath.md)
Method: [sanitizeFilename()](method-sanitizefilename.md)
Method: [supportsExec()](method-supportsexec.md)
