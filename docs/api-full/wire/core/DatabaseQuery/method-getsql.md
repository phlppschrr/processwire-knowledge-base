# $databaseQuery->getSQL($method = ''): string

Source: `wire/core/DatabaseQuery.php`

Return generated SQL for entire query or specific method

## Usage

~~~~~
// basic usage
$string = $databaseQuery->getSQL();

// usage with all arguments
$string = $databaseQuery->getSQL($method = '');
~~~~~

## Arguments

- `$method` (optional) `string` Optionally specify method name to get SQL for

## Return value

- `string`

## Since

3.0.157
