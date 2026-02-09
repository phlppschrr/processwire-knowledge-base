# PagesPathFinderTests

Source: `wire/core/PagesPathFinder.php`

Inherits: `Wire`

## Summary

PagesPathFinder Tests

Common methods:
- [`pathFinder()`](method-pathfinder.md)
- [`testPath()`](method-testpath.md)
- [`testPage()`](method-testpage.md)
- [`testPages()`](method-testpages.md)

Usage:
~~~~~
$tester = $pages->pathFinder()->tester();
$a = $tester->testPath('/path/to/page/');
$a = $tester->testPage(Page $page);
$a = $tester->testPages("has_parent!=2");
$a = $tester->testPages(PageArray $items);
~~~~~

## Methods
- [`pathFinder(): PagesPathFinder`](method-pathfinder.md)
- [`testPath(string $path, int $expectResponse = 0): array`](method-testpath.md)
- [`testPage(Page $item): array`](method-testpage.md)
- [`testPages(string|PageArray $selector): array`](method-testpages.md)
