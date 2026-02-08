# $pagerNav->__construct($totalItems, $itemsPerPage, $currentPage)

Source: `wire/modules/Markup/MarkupPagerNav/PagerNav.php`

Construct the PagerNav

## Arguments

- `$totalItems` `int` Total number of items in the list to be paginated.
- `$itemsPerPage` `int` The number of items you want to appear per page.
- `$currentPage` `int` The current page number (NOTE: 0 based, not 1 based)

## Throws

- WireException if given itemsPerPage of 0
