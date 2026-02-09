# $wireSaveableItemsLookup->getLoadQuery($selectors = null): DatabaseQuerySelect

Source: `wire/core/WireSaveableItemsLookup.php`

Get the DatabaseQuerySelect to perform the load operation of items

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $wireSaveableItemsLookup->getLoadQuery();

// usage with all arguments
$databaseQuerySelect = $wireSaveableItemsLookup->getLoadQuery($selectors = null);
~~~~~

## Arguments

- `$selectors` (optional) `Selectors|string|null` Selectors or a selector string to find, or NULL to load all.

## Return value

- `DatabaseQuerySelect`
