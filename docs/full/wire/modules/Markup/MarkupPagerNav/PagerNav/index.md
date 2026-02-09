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
Method: [__construct()](method-__construct.md)
Method: [getPager()](method-getpager.md)
Method: [setLabels()](method-setlabels.md)
