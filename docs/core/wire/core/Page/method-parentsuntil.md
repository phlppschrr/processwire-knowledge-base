# $page->parentsUntil($selector = '', $filter = ''): PageArray

Source: `wire/core/Page.php`

Return all parents from current page till the one matched by $selector

This duplicates the jQuery parentsUntil() function in ProcessWire.

## Arguments

- `$selector` (optional) `string|Page|array` May either be a selector sor Page to stop at. Results will not include this.
- `$filter` (optional) `string|array` Optional selector to filter matched pages by

## Return value

PageArray
