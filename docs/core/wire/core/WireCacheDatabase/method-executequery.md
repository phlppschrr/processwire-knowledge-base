# $wireCacheDatabase->executeQuery(\PDOStatement $query): bool

Source: `wire/core/WireCacheDatabase.php`

Execute query

## Usage

~~~~~
// basic usage
$bool = $wireCacheDatabase->executeQuery($query);

// usage with all arguments
$bool = $wireCacheDatabase->executeQuery(\PDOStatement $query);
~~~~~

## Arguments

- `$query` `\PDOStatement`

## Return value

- `bool`
