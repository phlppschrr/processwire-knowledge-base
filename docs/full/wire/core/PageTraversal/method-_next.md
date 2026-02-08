# $pageTraversal->_next(Page $page, $selector = '', array $options = array()): Page|NullPage|PageArray|int

Source: `wire/core/PageTraversal.php`

Provides the core logic for next, prev, nextAll, prevAll, nextUntil, prevUntil

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array|Selectors` Optional selector. When specified, will find nearest sibling(s) that match.
- `$options` (optional) `array` Options to modify behavior - `prev` (bool): When true, previous siblings will be returned rather than next siblings. - `all` (bool): If true, returns all nextAll or prevAll rather than just single sibling (default=false). - `until` (string): If specified, returns siblings until another is found matching the given selector (default=false). - `qty` (bool): If true, makes it return just the quantity that would match (default=false).

## Return value

Page|NullPage|PageArray|int Returns one of the following: - `PageArray` if the "all" or "until" option is specified. - `Page|NullPage` in other cases.
