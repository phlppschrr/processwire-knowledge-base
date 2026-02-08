# $pageFinder->___getQueryJoinPath(DatabaseQuerySelect $query, $selector)

Source: `wire/core/PageFinder.php`

Special case when requested value is path or URL

## Usage

~~~~~
// basic usage
$result = $pageFinder->___getQueryJoinPath($query, $selector);

// usage with all arguments
$result = $pageFinder->___getQueryJoinPath(DatabaseQuerySelect $query, $selector);
~~~~~

## Arguments

- `$query` `DatabaseQuerySelect`
- `$selector` `Selector`

## Exceptions

- `PageFinderSyntaxException`
