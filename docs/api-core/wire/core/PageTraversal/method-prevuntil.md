# $pageTraversal->prevUntil(Page $page, $selector = '', $filter = '', array $options = array()): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages prior to this one until matching the one specified

## Usage

~~~~~
// basic usage
$items = $pageTraversal->prevUntil($page);

// usage with all arguments
$items = $pageTraversal->prevUntil(Page $page, $selector = '', $filter = '', array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|Page|array` May either be a selector or Page to stop at. Results will not include this.
- `$filter` (optional) `string|array` Optional selector to filter matched pages by
- `$options` (optional) `array` Options to pass to the _next() method

## Return value

- `PageArray`
