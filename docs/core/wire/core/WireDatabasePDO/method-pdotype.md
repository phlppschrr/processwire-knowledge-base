# $wireDatabasePDO->pdoType(&$query, $getName = false): \PDO|string

Source: `wire/core/WireDatabasePDO.php`

Return correct PDO instance type (reader or writer) based on given statement

## Usage

~~~~~
// basic usage
$result = $wireDatabasePDO->pdoType($query);

// usage with all arguments
$result = $wireDatabasePDO->pdoType(&$query, $getName = false);
~~~~~

## Arguments

- `$query` `string|\PDOStatement`
- `$getName` (optional) `bool` Get name of PDO type rather than instance? (default=false)

## Return value

- `\PDO|string`
