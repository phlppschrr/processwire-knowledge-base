# $pageTraversal->prevAll(Page $page, $selector = '', array $options = array()): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages prior to this one, optionally matching a selector

## Arguments

- Page $page
- string|array|Selectors $selector Optional selector. When specified, will filter the found siblings.
- array $options Options to pass to the _next() method

## Return value

PageArray Returns all matching pages after this one.
