# PagesPathFinder::getShortcutPageNum()

Source: `wire/core/PagesPathFinder.php`

Identify shortcut pagination info

Returns found pagination number, or 1 if first pagination.
Extracts the pagination segment from the path.

@param string $path

@return array of [ pageNum, pageNumPrefix ]
