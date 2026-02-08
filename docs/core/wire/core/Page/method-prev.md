# $page->prev($selector = '', ?PageArray $siblings = null): Page|NullPage

Source: `wire/core/Page.php`

Return the previous sibling page

~~~~~
// Get the previous sibling
$sibling = $page->prev();

// Get the previous sibling having field "featured" with value of "1"
$sibling = $page->prev("featured=1");
~~~~~

## Arguments

- `$selector` (optional) `string|array` Optional selector. When specified, will find nearest previous sibling that matches.
- `$siblings` (optional) `PageArray|null` Optional siblings to use instead of the default.

## Return value

Page|NullPage Returns the previous sibling page, or a NullPage if none found.
