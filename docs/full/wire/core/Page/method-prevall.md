# $page->prevAll($selector = '', $getQty = false): Page|NullPage|int

Source: `wire/core/Page.php`

Return all sibling pages before this one, optionally matching a selector

## Arguments

- `$selector` (optional) `string|array|bool` Optional selector. When specified, will filter the found siblings.
- `$getQty` (optional) `bool|PageArray` Return a count instead of PageArray? (boolean) - If no $selector argument is needed, this may be specified as the first argument. - Legacy support: You may specify a PageArray of siblings to use instead of the default (deprecated, avoid it).

## Return value

Page|NullPage|int Returns all matching pages before this one, or integer if $getQty requested.
