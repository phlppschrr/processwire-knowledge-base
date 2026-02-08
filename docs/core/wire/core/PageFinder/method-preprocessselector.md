# $pageFinder->preProcessSelector(Selector $selector, Selectors $selectors, array $options, $level = 0): bool|Selector

Source: `wire/core/PageFinder.php`

Pre-process the given selector to perform any necessary replacements

This is primarily used to handle sub-selections, i.e. "bar=foo, id=[this=that, foo=bar]"
and OR-groups, i.e. "(bar=foo), (foo=bar)"

## Arguments

- Selector $selector
- Selectors $selectors
- array $options
- int $level

## Return value

bool|Selector Returns false if selector should be skipped over by getQuery(), returns Selector otherwise

## Throws

- PageFinderSyntaxException
