# $pageTraversal->prevUntilSiblings(Page $page, $selector = '', $filter = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages before this one until matching the one specified

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|Page|array` May either be a selector or Page to stop at. Results will not include this.
- `$filter` (optional) `string|array` Optional selector string to filter matched pages by
- `$siblings` (optional) `PageArray|null` Optional PageArray of siblings to use instead of all from the page.

## Return value

PageArray
