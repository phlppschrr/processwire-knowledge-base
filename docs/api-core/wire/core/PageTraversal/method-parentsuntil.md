# $pageTraversal->parentsUntil(Page $page, $selector = '', $filter = ''): PageArray

Source: `wire/core/PageTraversal.php`

Return all parent from current till the one matched by $selector

## Usage

~~~~~
// basic usage
$items = $pageTraversal->parentsUntil($page);

// usage with all arguments
$items = $pageTraversal->parentsUntil(Page $page, $selector = '', $filter = '');
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|Page|array` May either be a selector or Page to stop at. Results will not include this.
- `$filter` (optional) `string|array` Optional selector to filter matched pages by

## Return value

- `PageArray`
