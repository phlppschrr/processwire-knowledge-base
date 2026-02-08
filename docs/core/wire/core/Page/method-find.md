# Page::find()

Source: `wire/core/Page.php`

Find descendant pages matching given selector

This is the same as `Pages::find()` except that the results are limited to descendents of this Page.

~~~~~
// Find all unpublished pages underneath the current page
$items = $page->find("status=unpublished");
~~~~~


@param string|array $selector Selector string or array

@param array $options Same as the $options array passed to $pages->find().

@return PageArray

@see Pages::find()
