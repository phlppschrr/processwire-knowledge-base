# $wireDatabasePDOStatement->executeDebug($input_parameters = NULL): bool

Source: `wire/core/WireDatabasePDOStatement.php`

Execute prepared statement when in debug mode only

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDOStatement->executeDebug();

// usage with all arguments
$bool = $wireDatabasePDOStatement->executeDebug($input_parameters = NULL);
~~~~~

## Arguments

- `$input_parameters` (optional) `array|null`

## Return value

- `bool`

## Exceptions

- `\PDOException`
