# PageTraversal::next()

Source: `wire/core/PageTraversal.php`

Return the next sibling page

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will find nearest next sibling that matches.

@return Page|NullPage Returns the next sibling page, or a NullPage if none found.
