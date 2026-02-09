# $wireSaveableItems->getLoadQuery($selectors = null): DatabaseQuerySelect

Source: `wire/core/WireSaveableItems.php`

Get the DatabaseQuerySelect to perform the load operation of items

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $wireSaveableItems->getLoadQuery();

// usage with all arguments
$databaseQuerySelect = $wireSaveableItems->getLoadQuery($selectors = null);
~~~~~

## Arguments

- `$selectors` (optional) `Selectors|string|null` Selectors or a selector string to find, or NULL to load all.

## Return value

- `DatabaseQuerySelect`
