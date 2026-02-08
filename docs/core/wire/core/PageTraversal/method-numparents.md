# PageTraversal::numParents()

Source: `wire/core/PageTraversal.php`

Return number of parents (depth relative to homepage) that this page has, optionally filtered by a selector

For example, homepage has 0 parents and root level pages have 1 parent (which is the homepage), and the
number increases the deeper the page is in the pages structure.

@param Page $page

@param string $selector Optional selector to filter by (default='')

@return int Number of parents
