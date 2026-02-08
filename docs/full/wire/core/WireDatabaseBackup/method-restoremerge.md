# $wireDatabaseBackup->restoreMerge($filename1, $filename2, $options): bool

Source: `wire/core/WireDatabaseBackup.php`

Restore from 2 SQL files while resolving table differences (think of it as array_merge for a DB restore)

The CREATE TABLE and INSERT statements in filename2 take precedence of those in filename1.
INSERT statements from both will be executed, with filename2 INSERTs updating those of filename1.
CREATE TABLE statements in filename1 won't be executed if they also exist in filename2.

This method assumes both files follow the SQL dump format created by this class.

## Arguments

- string $filename1 Original filename
- string $filename2 Filename that may have statements that will update/override those in filename1
- array $options

## Return value

bool True on success, false on fail.

## Throws

- \Exception|WireException if $options['haltOnErrors'] == true.
