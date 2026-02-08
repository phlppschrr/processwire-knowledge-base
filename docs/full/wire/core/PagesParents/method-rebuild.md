# $pagesParents->rebuild(Page $page): int

Source: `wire/core/PagesParents.php`

Rebuild pages_parents table for given page

This descends into both parents, and children that are themselves parents,
and this method already calls the rebuildBranch() method when appropriate.

## Usage

~~~~~
// basic usage
$int = $pagesParents->rebuild($page);

// usage with all arguments
$int = $pagesParents->rebuild(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Return value

- `int`

## Since

3.0.156
