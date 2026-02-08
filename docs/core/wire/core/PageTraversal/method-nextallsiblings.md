# $pageTraversal->nextAllSiblings(Page $page, $selector = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages after this one, optionally matching a selector

## Arguments

- Page $page
- string|array $selector Optional selector. When specified, will filter the found siblings.
- PageArray|null $siblings Optional siblings to use instead of the default.

## Return value

PageArray Returns all matching pages after this one.
