# $page->child($selector = '', $options = array()): Page|NullPage

Source: `wire/core/Page.php`

Return the page’s first single child that matches the given selector.

Same as `$page->children()` but returns a single Page object or NullPage (with id=0) rather than a PageArray.
Meaning, this method will only ever return one Page.

~~~~~
// Get the newest created child page
$newestChild = $page->child("sort=-created");
~~~~~

## Arguments

- `$selector` (optional) `string|array|int` Selector to use, or blank to return the first child.
- `$options` (optional) `array` Optional options per Pages::find

## Return value

Page|NullPage

## See also

- [Page::children()](method-children.md)
