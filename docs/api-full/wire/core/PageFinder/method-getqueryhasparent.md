# $pageFinder->getQueryHasParent(DatabaseQuerySelect $query, $selector)

Source: `wire/core/PageFinder.php`

Make the query specific to all pages below a certain parent (children, grandchildren, great grandchildren, etc.)

## Usage

~~~~~
// basic usage
$result = $pageFinder->getQueryHasParent($query, $selector);

// usage with all arguments
$result = $pageFinder->getQueryHasParent(DatabaseQuerySelect $query, $selector);
~~~~~

## Arguments

- `$query` `DatabaseQuerySelect`
- `$selector` `Selector`
