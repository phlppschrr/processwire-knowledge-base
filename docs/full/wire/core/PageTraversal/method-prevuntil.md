# $pageTraversal->prevUntil(Page $page, $selector = '', $filter = '', array $options = array()): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages prior to this one until matching the one specified

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|Page|array` May either be a selector or Page to stop at. Results will not include this.
- `$filter` (optional) `string|array` Optional selector to filter matched pages by
- `$options` (optional) `array` Options to pass to the _next() method

## Return value

PageArray
