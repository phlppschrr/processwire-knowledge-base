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

## pathFinder()

@return PagesPathFinder

## testPath()

@param string $path

@param int $expectResponse

@return array

## testPage()

@param Page $item

@return array

## testPages()

@param string|PageArray $selector

@return array
