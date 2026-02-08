# PageTraversal::child()

Source: `wire/core/PageTraversal.php`

Return the page's first single child that matches the given selector.

Same as children() but returns a Page object or NullPage (with id=0) rather than a PageArray

@param Page $page

@param string|array $selector Selector to use, or blank to return the first child.

@param array $options

@return Page|NullPage
