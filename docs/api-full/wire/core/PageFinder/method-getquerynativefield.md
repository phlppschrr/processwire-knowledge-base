# $pageFinder->getQueryNativeField(DatabaseQuerySelect $query, $selector, $fields, array $options, $selectors)

Source: `wire/core/PageFinder.php`

Special case when field is native to the pages table

TODO not all operators will work here, so may want to add some translation or filtering

## Usage

~~~~~
// basic usage
$result = $pageFinder->getQueryNativeField($query, $selector, $fields, $options, $selectors);

// usage with all arguments
$result = $pageFinder->getQueryNativeField(DatabaseQuerySelect $query, $selector, $fields, array $options, $selectors);
~~~~~

## Arguments

- `$query` `DatabaseQuerySelect`
- `$selector` `Selector`
- `$fields` `array`
- `$options` `array`
- `$selectors` `Selectors`

## Exceptions

- `PageFinderSyntaxException`
