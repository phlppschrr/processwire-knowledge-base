# $pagesPathFinder->getPage($path, array $options = array()): NullPage|Page

Source: `wire/core/PagesPathFinder.php`

Given a path, get a Page object or NullPage if not found

This method is like the `get()` method except that it returns a `Page`
object rather than an array. It sets a `_pagePathFinder` property to the
returned Page, which is an associative array containing the same result
array returned by the `get()` method.

Please access this method from `$pages->pathFinder()->getPage('…');`

## Arguments

- string $path
- array $options

## Return value

NullPage|Page

## See also

- [PagesPathFinder::get()](method-get.md)
