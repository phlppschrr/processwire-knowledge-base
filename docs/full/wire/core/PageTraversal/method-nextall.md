# $pageTraversal->nextAll(Page $page, $selector = '', array $options = array()): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages after this one, optionally matching a selector

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array|Selectors` Optional selector. When specified, will filter the found siblings.
- `$options` (optional) `array` Options to pass to the _next() method

## Return value

PageArray Returns all matching pages after this one.
