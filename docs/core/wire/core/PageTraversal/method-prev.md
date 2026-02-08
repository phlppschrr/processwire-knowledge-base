# PageTraversal::prev()

Source: `wire/core/PageTraversal.php`

Return the previous sibling page

@param Page $page

@param string|array|Selectors $selector Optional selector. When specified, will find nearest previous sibling that matches.

@return Page|NullPage Returns the previous sibling page, or a NullPage if none found.
