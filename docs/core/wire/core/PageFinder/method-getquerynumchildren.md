# $pageFinder->getQueryNumChildren(DatabaseQuerySelect $query, $selector): string

Source: `wire/core/PageFinder.php`

Match a number of children count

## Usage

~~~~~
// basic usage
$string = $pageFinder->getQueryNumChildren($query, $selector);

// usage with all arguments
$string = $pageFinder->getQueryNumChildren(DatabaseQuerySelect $query, $selector);
~~~~~

## Arguments

- `$query` `DatabaseQuerySelect`
- `$selector` `Selector`

## Return value

- `string`

## Exceptions

- `WireException`
