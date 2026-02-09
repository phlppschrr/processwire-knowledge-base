# $databaseQuery->execute(array $options = array()): \PDOStatement|bool

Source: `wire/core/DatabaseQuery.php`

Execute the query with the current database handle

## Usage

~~~~~
// basic usage
$result = $databaseQuery->execute();

// usage with all arguments
$result = $databaseQuery->execute(array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` - `throw` (bool): Throw exceptions? (default=true) - `maxTries` (int): Max times to retry if connection lost during query. (default=3) - `returnQuery` (bool): Return PDOStatement query? If false, returns bool result of execute. (default=true)

## Return value

- `\PDOStatement|bool`

## Exceptions

- `WireDatabaseQueryException|\PDOException`
