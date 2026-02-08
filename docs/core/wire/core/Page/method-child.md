# Page::child()

Source: `wire/core/Page.php`

Return the page’s first single child that matches the given selector.

Same as `$page->children()` but returns a single Page object or NullPage (with id=0) rather than a PageArray.
Meaning, this method will only ever return one Page.

~~~~~
// Get the newest created child page
$newestChild = $page->child("sort=-created");
~~~~~


@param string|array|int $selector Selector to use, or blank to return the first child.

@param array $options Optional options per Pages::find

@return Page|NullPage

@see Page::children()
