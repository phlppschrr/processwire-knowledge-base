# PagerNav::__construct()

Source: `wire/modules/Markup/MarkupPagerNav/PagerNav.php`

Construct the PagerNav

@param int $totalItems Total number of items in the list to be paginated.

@param int $itemsPerPage The number of items you want to appear per page.

@param int $currentPage The current page number (NOTE: 0 based, not 1 based)

@throws WireException if given itemsPerPage of 0
