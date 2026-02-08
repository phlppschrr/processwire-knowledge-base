# $page->nextAll($selector = '', $getQty = false, $getPrev = false): PageArray|int

Source: `wire/core/Page.php`

Return all sibling pages after this one, optionally matching a selector

## Usage

~~~~~
// basic usage
$items = $page->nextAll();

// usage with all arguments
$items = $page->nextAll($selector = '', $getQty = false, $getPrev = false);
~~~~~

## Arguments

- `$selector` (optional) `string|array|bool` Optional selector. When specified, will filter the found siblings.
- `$getQty` (optional) `bool|PageArray` Return a count instead of PageArray? (boolean) - If no $selector argument is needed, this may be specified as the first argument. - Legacy support: You may specify a PageArray of siblings to use instead of the default (deprecated, avoid it).
- `$getPrev` (optional) `bool` For internal use, makes this method implement the prevAll() behavior instead.

## Return value

- `PageArray|int` Returns all matching pages after this one, or integer if $count option specified.
