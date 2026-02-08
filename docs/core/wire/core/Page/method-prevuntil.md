# $page->prevUntil($selector = '', $filter = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/Page.php`

Return all sibling pages before this one until matching the one specified

## Arguments

- `$selector` (optional) `string|Page|array` May either be a selector or Page to stop at. Results will not include this.
- `$filter` (optional) `string|array` Optional selector to filter matched pages by
- `$siblings` (optional) `PageArray|null` Optional PageArray of siblings to use instead of default.

## Return value

PageArray
