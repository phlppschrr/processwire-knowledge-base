# $pagesParents->rebuild(Page $page): int

Source: `wire/core/PagesParents.php`

Rebuild pages_parents table for given page

This descends into both parents, and children that are themselves parents,
and this method already calls the rebuildBranch() method when appropriate.

## Arguments

- Page $page

## Return value

int

## Meta

- @since 3.0.156
