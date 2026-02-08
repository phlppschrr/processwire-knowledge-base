# $page->next($selector = '', ?PageArray $siblings = null): Page|NullPage

Source: `wire/core/Page.php`

Return the next sibling page

By default, hidden, unpublished and non-viewable pages are excluded. If you want them included,
be sure to specify `include=` with hidden, unpublished or all, in your selector.

~~~~~
// Get the next sibling
$sibling = $page->next();

// Get the next newest sibling
$sibling = $page->next("created>$page->created");

// Get the next sibling, even if it isn't viewable
$sibling = $page->next("include=all");
~~~~~

## Arguments

- string|array $selector Optional selector. When specified, will find nearest next sibling that matches.
- PageArray $siblings Optional siblings to use instead of the default. Avoid using this argument as it forces this method to use the older/slower functions.

## Return value

Page|NullPage Returns the next sibling page, or a NullPage if none found.
