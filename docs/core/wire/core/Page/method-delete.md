# Page::delete()

Source: `wire/core/Page.php`

Delete this page from the database

This is the same as calling `$pages->delete($page)`.

~~~~~
// Delete pages named "delete-me" that don't have children
$items = $pages->find("name=delete-me, numChildren=0");
foreach($items as $item) {
  $item->delete();
}
~~~~~
~~~~~
// Delete a page and recursively all of its children, grandchildren, etc.
$item = $pages->get('/some-page/');
$item->delete(true);
~~~~~


@param bool $recursive If set to true, then this will attempt to delete all children too.

@return bool|int True on success, false on failure, or int quantity of pages deleted when recursive option is true.

@throws WireException when attempting to delete a page with children and $recursive option is not specified.

@see Pages::delete()
