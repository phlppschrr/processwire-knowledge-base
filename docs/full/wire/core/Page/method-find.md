# $page->find($selector = '', $options = array()): PageArray

Source: `wire/core/Page.php`

Find descendant pages matching given selector

This is the same as `Pages::find()` except that the results are limited to descendents of this Page.

~~~~~
// Find all unpublished pages underneath the current page
$items = $page->find("status=unpublished");
~~~~~

## Arguments

- string|array $selector Selector string or array
- array $options Same as the $options array passed to $pages->find().

## Return value

PageArray

## See also

- [Pages::find()](../Pages/method-___find.md)
