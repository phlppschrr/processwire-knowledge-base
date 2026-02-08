# PagesPathFinder::getPage()

Source: `wire/core/PagesPathFinder.php`

Given a path, get a Page object or NullPage if not found

This method is like the `get()` method except that it returns a `Page`
object rather than an array. It sets a `_pagePathFinder` property to the
returned Page, which is an associative array containing the same result
array returned by the `get()` method.

Please access this method from `$pages->pathFinder()->getPage('…');`

@param string $path

@param array $options

@return NullPage|Page

@see PagesPathFinder::get()
