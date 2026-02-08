# $fieldgroups->getLoadQuery($selectors = null): DatabaseQuerySelect

Source: `wire/core/Fieldgroups.php`

Get the DatabaseQuerySelect to perform the load operation of items

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $fieldgroups->getLoadQuery();

// usage with all arguments
$databaseQuerySelect = $fieldgroups->getLoadQuery($selectors = null);
~~~~~

## Arguments

- `$selectors` (optional) `Selectors|string|null` Selectors or a selector string to find, or NULL to load all.

## Return value

- `DatabaseQuerySelect`
