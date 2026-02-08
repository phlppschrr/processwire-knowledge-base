# PageTraversal::prevAll()

Source: `wire/core/PageTraversal.php`

Return all sibling pages prior to this one, optionally matching a selector

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will filter the found siblings.

@param array $options Options to pass to the _next() method

@return PageArray Returns all matching pages after this one.
