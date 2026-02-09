# $wireDatabaseBackup->executeQuery($query, $options = array()): bool

Source: `wire/core/WireDatabaseBackup.php`

Execute an SQL query, either a string or PDOStatement

## Usage

~~~~~
// basic usage
$bool = $wireDatabaseBackup->executeQuery($query);

// usage with all arguments
$bool = $wireDatabaseBackup->executeQuery($query, $options = array());
~~~~~

## Arguments

- `$query` `string|\PDOStatement`
- `$options` (optional) `bool|array` May be boolean (for haltOnError), or array containing the property (i.e. $options array) - `haltOnError` (bool): Halt execution when error occurs? (default=false)

## Return value

- `bool` Query result

## Exceptions

- `\Exception` if haltOnError, otherwise it populates $this->errors
