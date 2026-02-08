# PageFinder::preProcessSelector()

Source: `wire/core/PageFinder.php`

Pre-process the given selector to perform any necessary replacements

This is primarily used to handle sub-selections, i.e. "bar=foo, id=[this=that, foo=bar]"
and OR-groups, i.e. "(bar=foo), (foo=bar)"

@param Selector $selector

@param Selectors $selectors

@param array $options

@param int $level

@return bool|Selector Returns false if selector should be skipped over by getQuery(), returns Selector otherwise

@throws PageFinderSyntaxException
