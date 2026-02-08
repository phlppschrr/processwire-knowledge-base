# $pageFinder->getQuery($selectors, array $options): DatabaseQuerySelect

Source: `wire/core/PageFinder.php`

Given one or more selectors, create the SQL query for finding pages.

## Usage

~~~~~
// basic usage
$databaseQuerySelect = $pageFinder->getQuery($selectors, $options);

// usage with all arguments
$databaseQuerySelect = $pageFinder->getQuery($selectors, array $options);
~~~~~

## Hookable

- Hookable method name: `getQuery`
- Implementation: `___getQuery`
- Hook with: `$pageFinder->getQuery()`

## Arguments

- `$selectors` `Selectors` Array of selectors.
- `$options` `array`

## Return value

- `DatabaseQuerySelect`

## Exceptions

- `PageFinderSyntaxException`

## Details

- @TODO split this method up into more parts, it's too long
