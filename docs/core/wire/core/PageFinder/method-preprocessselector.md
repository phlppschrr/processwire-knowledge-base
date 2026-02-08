# $pageFinder->preProcessSelector(Selector $selector, Selectors $selectors, array $options, $level = 0): bool|Selector

Source: `wire/core/PageFinder.php`

Pre-process the given selector to perform any necessary replacements

This is primarily used to handle sub-selections, i.e. "bar=foo, id=[this=that, foo=bar]"
and OR-groups, i.e. "(bar=foo), (foo=bar)"

## Usage

~~~~~
// basic usage
$bool = $pageFinder->preProcessSelector($selector, $selectors, $options);

// usage with all arguments
$bool = $pageFinder->preProcessSelector(Selector $selector, Selectors $selectors, array $options, $level = 0);
~~~~~

## Arguments

- `$selector` `Selector`
- `$selectors` `Selectors`
- `$options` `array`
- `$level` (optional) `int`

## Return value

- `bool|Selector` Returns false if selector should be skipped over by getQuery(), returns Selector otherwise

## Exceptions

- `PageFinderSyntaxException`
