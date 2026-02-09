# $pageTraversal->child(Page $page, $selector = '', $options = array()): Page|NullPage

Source: `wire/core/PageTraversal.php`

Return the page's first single child that matches the given selector.

Same as children() but returns a Page object or NullPage (with id=0) rather than a PageArray

## Usage

~~~~~
// basic usage
$page = $pageTraversal->child($page);

// usage with all arguments
$page = $pageTraversal->child(Page $page, $selector = '', $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array` Selector to use, or blank to return the first child.
- `$options` (optional) `array`

## Return value

- `Page|NullPage`
