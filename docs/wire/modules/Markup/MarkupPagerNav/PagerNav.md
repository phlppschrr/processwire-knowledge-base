# PagerNav

Source: `wire/modules/Markup/MarkupPagerNav/PagerNav.php`

Collection of Pager items that determines which pagination links should be used

USAGE EXAMPLE:

$pager = new PagerNav(100, 10, 0);

foreach($pager as $pageLabel => $pageNum) {
	$class = "action";
	if($pageNum == $pager->getCurrentPage()) $class .= " on";
	$out .= "<li><a class='$class' href='$baseUrl$pageNum/'>$pageLabel</a></li>";
}

## __construct()

Construct the PagerNav

@param int $totalItems Total number of items in the list to be paginated.

@param int $itemsPerPage The number of items you want to appear per page.

@param int $currentPage The current page number (NOTE: 0 based, not 1 based)

@throws WireException if given itemsPerPage of 0

## getPager()

Returns an array contantaining $label => $pageNum

Rather than access this function directly, it is prefereable to iterate the object.

@return array

## setLabels()

Set the labels to use for the 'prev' and 'next' links

@param string $previous 'Previous' label

@param string $next 'Next' label
