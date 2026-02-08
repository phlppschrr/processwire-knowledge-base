# $pageTraversal->parents(Page $page, $selector = ''): PageArray

Source: `wire/core/PageTraversal.php`

Return this page's parent pages, or the parent pages matching the given selector.

## Usage

~~~~~
// basic usage
$items = $pageTraversal->parents($page);

// usage with all arguments
$items = $pageTraversal->parents(Page $page, $selector = '');
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string|array|bool` Optional selector string to filter parents by or boolean true for reverse order

## Return value

- `PageArray`
