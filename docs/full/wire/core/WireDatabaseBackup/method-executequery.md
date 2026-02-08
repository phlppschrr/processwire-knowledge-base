# $wireDatabaseBackup->executeQuery($query, $options = array()): bool

Source: `wire/core/WireDatabaseBackup.php`

Execute an SQL query, either a string or PDOStatement

## Arguments

- string|\PDOStatement $query
- bool|array $options May be boolean (for haltOnError), or array containing the property (i.e. $options array) - `haltOnError` (bool): Halt execution when error occurs? (default=false)

## Return value

bool Query result

## Throws

- \Exception if haltOnError, otherwise it populates $this->errors
