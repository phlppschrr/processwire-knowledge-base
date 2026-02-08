# $pageTraversal->nextUntilSiblings(Page $page, $selector = '', $filter = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages after this one until matching the one specified

## Usage

~~~~~
// basic usage
$items = $pageTraversal->nextUntilSiblings($page);

// usage with all arguments
$items = $pageTraversal->nextUntilSiblings(Page $page, $selector = '', $filter = '', ?PageArray $siblings = null);
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|Page|array` May either be a selector or Page to stop at. Results will not include this.
- `$filter` (optional) `string|array` Optional selector to filter matched pages by
- `$siblings` (optional) `PageArray|null` Optional PageArray of siblings to use instead of all from the page.

## Return value

- `PageArray`
