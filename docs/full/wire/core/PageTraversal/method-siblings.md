# $pageTraversal->siblings(Page $page, $selector = ''): PageArray

Source: `wire/core/PageTraversal.php`

Return this Page's sibling pages, optionally filtered by a selector.

Note that the siblings include the current page. To exclude the current page, specify "id!=$page".

## Arguments

- `$page` `Page`
- `$selector` (optional) `string` Optional selector to filter siblings by.

## Return value

PageArray
