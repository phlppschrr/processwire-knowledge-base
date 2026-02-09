# $pageTraversal->numLinks(Page $page, $field = false): int

Source: `wire/core/PageTraversal.php`

Return total found number of pages linking to this one with no exclusions

## Usage

~~~~~
// basic usage
$int = $pageTraversal->numLinks($page);

// usage with all arguments
$int = $pageTraversal->numLinks(Page $page, $field = false);
~~~~~

## Arguments

- `$page` `Page`
- `$field` (optional) `bool`

## Return value

- `int`
