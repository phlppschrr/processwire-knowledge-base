# $pageFinder->getQueryJoinPath(DatabaseQuerySelect $query, $selector)

Source: `wire/core/PageFinder.php`

Special case when requested value is path or URL

## Usage

~~~~~
// basic usage
$result = $pageFinder->getQueryJoinPath($query, $selector);

// usage with all arguments
$result = $pageFinder->getQueryJoinPath(DatabaseQuerySelect $query, $selector);
~~~~~

## Hookable

- Hookable method name: `getQueryJoinPath`
- Implementation: `___getQueryJoinPath`
- Hook with: `$pageFinder->getQueryJoinPath()`

## Arguments

- `$query` `DatabaseQuerySelect`
- `$selector` `Selector`

## Exceptions

- `PageFinderSyntaxException`
