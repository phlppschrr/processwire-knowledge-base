# $pageFinder->getMatchQueryJSON(DatabaseQuerySelect $q, $tableAlias, $subfields, $operator, $value): bool

Source: `wire/core/PageFinder.php`

Get match query when data is stored in a JSON DB column (future use)

## Usage

~~~~~
// basic usage
$bool = $pageFinder->getMatchQueryJSON($q, $tableAlias, $subfields, $operator, $value);

// usage with all arguments
$bool = $pageFinder->getMatchQueryJSON(DatabaseQuerySelect $q, $tableAlias, $subfields, $operator, $value);
~~~~~

## Arguments

- PageFinderDatabaseQuerySelect DatabaseQuerySelect $q
- `$tableAlias` `string`
- `$subfields` `string`
- `$operator` `string`
- `$value` `string|int|array`

## Return value

- `bool`
