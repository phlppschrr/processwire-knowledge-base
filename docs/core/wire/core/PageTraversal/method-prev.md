# $pageTraversal->prev(Page $page, $selector = ''): Page|NullPage

Source: `wire/core/PageTraversal.php`

Return the previous sibling page

## Usage

~~~~~
// basic usage
$page = $pageTraversal->prev($page);

// usage with all arguments
$page = $pageTraversal->prev(Page $page, $selector = '');
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array|Selectors` Optional selector. When specified, will find nearest previous sibling that matches.

## Return value

- `Page|NullPage` Returns the previous sibling page, or a NullPage if none found.
