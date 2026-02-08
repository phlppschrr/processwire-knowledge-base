# $pagerNav->__construct($totalItems, $itemsPerPage, $currentPage)

Source: `wire/modules/Markup/MarkupPagerNav/PagerNav.php`

Construct the PagerNav

## Arguments

- int $totalItems Total number of items in the list to be paginated.
- int $itemsPerPage The number of items you want to appear per page.
- int $currentPage The current page number (NOTE: 0 based, not 1 based)

## Throws

- WireException if given itemsPerPage of 0
