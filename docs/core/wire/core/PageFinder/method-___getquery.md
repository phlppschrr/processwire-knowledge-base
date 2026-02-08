# $pageFinder->___getQuery($selectors, array $options): DatabaseQuerySelect

Source: `wire/core/PageFinder.php`

Given one or more selectors, create the SQL query for finding pages.

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $pageFinder->___getQuery($selectors, $options);

// usage with all arguments
$databaseQuerySelect = $pageFinder->___getQuery($selectors, array $options);
~~~~~

## Arguments

- `$selectors` `Selectors` Array of selectors.
- `$options` `array`

## Return value

- `DatabaseQuerySelect`

## Exceptions

- `PageFinderSyntaxException`

## Details

- @TODO split this method up into more parts, it's too long
