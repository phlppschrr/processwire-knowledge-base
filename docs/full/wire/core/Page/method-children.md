# $page->children($selector = '', $options = array()): PageArray|array

Source: `wire/core/Page.php`

Return this page’s children, optionally filtered by a selector

By default, hidden, unpublished and no-access pages are excluded unless `include=x` (where "x" is desired status) is specified.
If a selector isn't needed, children can also be accessed directly by property with `$page->children`.

~~~~~
// Render navigation for all child pages below this one
foreach($page->children() as $child) {
  echo "<li><a href='$child->url'>$child->title</a></li>";
}
~~~~~
~~~~~
// Retrieve just the 3 newest children
$newest = $page->children("limit=3, sort=-created");
~~~~~

## Arguments

- `$selector` (optional) `string` Selector to use, or omit to return all children.
- `$options` (optional) `array` Optional options to modify behavior, the same as those provided to Pages::find.

## Return value

PageArray|array Returns PageArray for most cases. Returns regular PHP array if using the findIDs option.

## See also

- [Page::child()](method-child.md)
- [Page::find()](method-find.md)
- [Page::numChildren()](method-numchildren.md)
- [Page::hasChildren()](method-haschildren.md)
