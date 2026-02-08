# PageTraversal::prevAllSiblings()

Source: `wire/core/PageTraversal.php`

Return all sibling pages before this one, optionally matching a selector

@param Page $page

@param string|array $selector Optional selector. When specified, will filter the found siblings.

@param PageArray|null $siblings Optional siblings to use instead of the default.

@return PageArray
