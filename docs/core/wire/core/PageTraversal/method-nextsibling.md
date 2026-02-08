# $pageTraversal->nextSibling(Page $page, $selector = '', ?PageArray $siblings = null): Page|NullPage

Source: `wire/core/PageTraversal.php`

Return the next sibling page, within a group of provided siblings (that includes the current page)

This method is the old version of the next() method and is only used if a $siblings argument is provided
to the Page::next() call.  It is much slower than the next() method.

If given a PageArray of siblings (containing the current) it will return the next sibling relative to the provided PageArray.

Be careful with this function when the page has a lot of siblings. It has to load them all, so this function is best
avoided at large scale, unless you provide your own already-reduced siblings list (like from pagination)

When using a selector, note that this method operates only on visible children. If you want something like "include=all"
or "include=hidden", they will not work in the selector. Instead, you should provide the siblings already retrieved with
one of those modifiers, and provide those siblings as the second argument to this function.

## Usage

~~~~~
// basic usage
$page = $pageTraversal->nextSibling($page);

// usage with all arguments
$page = $pageTraversal->nextSibling(Page $page, $selector = '', ?PageArray $siblings = null);
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array` Optional selector. When specified, will find nearest next sibling that matches.
- `$siblings` (optional) `PageArray|null` Optional siblings to use instead of the default. May also be specified as first argument when no selector needed.

## Return value

- `Page|NullPage` Returns the next sibling page, or a NullPage if none found.
