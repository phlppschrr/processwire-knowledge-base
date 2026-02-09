# PagerNav

Source: `wire/modules/Markup/MarkupPagerNav/PagerNav.php`

Implements: `IteratorAggregate`

Collection of Pager items that determines which pagination links should be used

USAGE EXAMPLE:

```php
$pager = new PagerNav(100, 10, 0);

foreach($pager as $pageLabel => $pageNum) {
	$class = "action";
	if($pageNum == $pager->getCurrentPage()) $class .= " on";
	$out .= "<li><a class='$class' href='$baseUrl$pageNum/'>$pageLabel</a></li>";
}
```

Methods:
- [`__construct(int $totalItems, int $itemsPerPage, int $currentPage)`](method-__construct.md)
- [`getPager(): array`](method-getpager.md)
- [`setLabels(string $previous, string $next)`](method-setlabels.md)
