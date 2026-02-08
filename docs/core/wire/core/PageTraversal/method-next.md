# $pageTraversal->next(Page $page, $selector = ''): Page|NullPage

Source: `wire/core/PageTraversal.php`

Return the next sibling page

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array|Selectors` Optional selector. When specified, will find nearest next sibling that matches.

## Return value

Page|NullPage Returns the next sibling page, or a NullPage if none found.
