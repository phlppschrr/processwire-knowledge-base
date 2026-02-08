# $wireSaveableItems->getLoadQuerySelectors($selectors, DatabaseQuerySelect $query): DatabaseQuerySelect

Source: `wire/core/WireSaveableItems.php`

Provides additions to the ___load query for when selectors or selector string are provided

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $wireSaveableItems->getLoadQuerySelectors($selectors, $query);

// usage with all arguments
$databaseQuerySelect = $wireSaveableItems->getLoadQuerySelectors($selectors, DatabaseQuerySelect $query);
~~~~~

## Arguments

- `$selectors` `Selectors`
- `$query` `DatabaseQuerySelect`

## Return value

- `DatabaseQuerySelect`

## Exceptions

- `WireException`
