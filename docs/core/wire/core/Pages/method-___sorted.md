# $pages->___sorted(Page $page, $children = false, $total = 0)

Source: `wire/core/Pages.php`

Hook called after a page has been sorted, or had its children re-sorted

## Usage

~~~~~
// basic usage
$result = $pages->___sorted($page);

// usage with all arguments
$result = $pages->___sorted(Page $page, $children = false, $total = 0);
~~~~~

## Arguments

- `$page` `Page` Page given to have sort adjusted
- `$children` (optional) `bool` If true, children of $page have been all been re-sorted
- `$total` (optional) `int` Total number of pages that had sort adjusted as a result
