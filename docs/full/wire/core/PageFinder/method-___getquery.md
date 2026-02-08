# PageFinder::___getQuery()

Source: `wire/core/PageFinder.php`

Given one or more selectors, create the SQL query for finding pages.

@TODO split this method up into more parts, it's too long

@param Selectors $selectors Array of selectors.

@param array $options

@return DatabaseQuerySelect

@throws PageFinderSyntaxException
