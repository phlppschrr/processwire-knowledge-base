# $pageTraversal->children(Page $page, $selector = '', $options = array()): PageArray

Source: `wire/core/PageTraversal.php`

Return this page's children pages, optionally filtered by a selector

## Usage

~~~~~
// basic usage
$items = $pageTraversal->children($page);

// usage with all arguments
$items = $pageTraversal->children(Page $page, $selector = '', $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array` Selector to use, or blank to return all children
- `$options` (optional) `array`

## Return value

- `PageArray`
