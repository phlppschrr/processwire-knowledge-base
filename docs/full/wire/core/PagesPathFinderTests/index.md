# PagesPathFinderTests

Source: `wire/core/PagesPathFinder.php`

PagesPathFinder Tests

Usage:
~~~~~
$tester = $pages->pathFinder()->tester();
$a = $tester->testPath('/path/to/page/');
$a = $tester->testPage(Page $page);
$a = $tester->testPages("has_parent!=2");
$a = $tester->testPages(PageArray $items);
~~~~~

Methods:
Method: [pathFinder()](method-pathfinder.md)
Method: [testPath()](method-testpath.md)
Method: [testPage()](method-testpage.md)
Method: [testPages()](method-testpages.md)
