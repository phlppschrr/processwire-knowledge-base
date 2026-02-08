# $pageTraversal->prevAllSiblings(Page $page, $selector = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages before this one, optionally matching a selector

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array` Optional selector. When specified, will filter the found siblings.
- `$siblings` (optional) `PageArray|null` Optional siblings to use instead of the default.

## Return value

PageArray
