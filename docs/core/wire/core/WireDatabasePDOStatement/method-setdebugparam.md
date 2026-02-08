# $wireDatabasePDOStatement->setDebugParam($parameter, $value, $data_type = null)

Source: `wire/core/WireDatabasePDOStatement.php`

Set a named debug parameter

## Usage

~~~~~
// basic usage
$result = $wireDatabasePDOStatement->setDebugParam($parameter, $value);

// usage with all arguments
$result = $wireDatabasePDOStatement->setDebugParam($parameter, $value, $data_type = null);
~~~~~

## Arguments

- `$parameter` `string`
- `$value` `int|string|null`
- `$data_type` (optional) `int|null` \PDO::PARAM_* type
