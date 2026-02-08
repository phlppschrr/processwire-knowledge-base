# $pagesParents->descendents(Page $page, $selector = 'include=all'): PageArray

Source: `wire/core/PagesParents.php`

Find descendents of $page by going recursive rather than using pages_parents table (for testing)

## Usage

~~~~~
// basic usage
$items = $pagesParents->descendents($page);

// usage with all arguments
$items = $pagesParents->descendents(Page $page, $selector = 'include=all');
~~~~~

## Arguments

- `$page` `Page`
- `$selector` (optional) `string`

## Return value

- `PageArray`
