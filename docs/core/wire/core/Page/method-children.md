# Page::children()

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


@param string $selector Selector to use, or omit to return all children.

@param array $options Optional options to modify behavior, the same as those provided to Pages::find.

@return PageArray|array Returns PageArray for most cases. Returns regular PHP array if using the findIDs option.

@see Page::child(), Page::find(), Page::numChildren(), Page::hasChildren()
