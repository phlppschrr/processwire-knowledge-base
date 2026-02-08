# $page->parents($selector = ''): PageArray

Source: `wire/core/Page.php`

Return this page’s parent pages, or the parent pages matching the given selector.

This method returns all parents of this page, in order. If a selector is specified, they
will be filtered by the selector. By default, parents are returned in breadcrumb order.
In 3.0.158+ if you specify boolean true for selector argument, then it will return parents
in reverse order (closest to furthest).

~~~~~
// Render breadcrumbs
foreach($page->parents() as $parent) {
  echo "<li><a href='$parent->url'>$parent->title</a></li>";
}
~~~~~
~~~~~
// Return all parents, excluding the homepage
$parents = $page->parents("template!=home");
~~~~~
~~~~~
// Return parents in reverse order (closest to furthest, 3.0.158+)
$parents = $page->parents(true);
~~~~~

## Arguments

- string|array|bool $selector Optional selector string to filter parents by or boolean true for reverse order

## Return value

PageArray All parent pages, or those matching the given selector.
