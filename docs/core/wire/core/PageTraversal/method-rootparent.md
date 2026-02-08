# $pageTraversal->rootParent(Page $page): Page

Source: `wire/core/PageTraversal.php`

Get the lowest-level, non-homepage parent of this page

rootParents typically comprise the first level of navigation on a site.

## Usage

~~~~~
// basic usage
$page = $pageTraversal->rootParent($page);

// usage with all arguments
$page = $pageTraversal->rootParent(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `Page`
