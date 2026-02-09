# $wireDatabasePDOStatement->execute($input_parameters = NULL): bool

Source: `wire/core/WireDatabasePDOStatement.php`

Execute prepared statement

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDOStatement->execute();

// usage with all arguments
$bool = $wireDatabasePDOStatement->execute($input_parameters = NULL);
~~~~~

## Arguments

- `$input_parameters` (optional) `array|null`

## Return value

- `bool`

## Exceptions

- `\PDOException`
