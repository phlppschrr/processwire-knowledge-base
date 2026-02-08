# $wireDatabasePDOStatement->bindValue($parameter, $value, $data_type = \PDO::PARAM_STR): bool

Source: `wire/core/WireDatabasePDOStatement.php`

Bind a value for this statement

## Usage

~~~~~
// basic usage
$bool = $wireDatabasePDOStatement->bindValue($parameter, $value);

// usage with all arguments
$bool = $wireDatabasePDOStatement->bindValue($parameter, $value, $data_type = \PDO::PARAM_STR);
~~~~~

## Arguments

- `$parameter` `string|int`
- `$value` `mixed`
- `$data_type` (optional) `int`

## Return value

- `bool`
