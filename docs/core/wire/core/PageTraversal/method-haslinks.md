# $pageTraversal->hasLinks(Page $page, $field = false): array|int|PageArray

Source: `wire/core/PageTraversal.php`

Return total number of pages visible to current user linking to this one

## Usage

~~~~~
// basic usage
$array = $pageTraversal->hasLinks($page);

// usage with all arguments
$array = $pageTraversal->hasLinks(Page $page, $field = false);
~~~~~

## Arguments

- `$page` `Page`
- `$field` (optional) `bool`

## Return value

- `array|int|PageArray`
