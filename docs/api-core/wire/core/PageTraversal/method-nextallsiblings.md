# $pageTraversal->nextAllSiblings(Page $page, $selector = '', ?PageArray $siblings = null): PageArray

Source: `wire/core/PageTraversal.php`

Return all sibling pages after this one, optionally matching a selector

## Usage

~~~~~
// basic usage
$items = $pageTraversal->nextAllSiblings($page);

// usage with all arguments
$items = $pageTraversal->nextAllSiblings(Page $page, $selector = '', ?PageArray $siblings = null);
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array` Optional selector. When specified, will filter the found siblings.
- `$siblings` (optional) `PageArray|null` Optional siblings to use instead of the default.

## Return value

- `PageArray` Returns all matching pages after this one.
