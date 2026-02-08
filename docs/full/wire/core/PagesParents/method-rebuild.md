# PagesParents::rebuild()

Source: `wire/core/PagesParents.php`

Rebuild pages_parents table for given page

This descends into both parents, and children that are themselves parents,
and this method already calls the rebuildBranch() method when appropriate.

@param Page $page

@return int

@since 3.0.156
