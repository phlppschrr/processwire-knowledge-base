# $pagesPathFinder->getShortcutPageNum(&$path): array

Source: `wire/core/PagesPathFinder.php`

Identify shortcut pagination info

Returns found pagination number, or 1 if first pagination.
Extracts the pagination segment from the path.

## Usage

~~~~~
// basic usage
$array = $pagesPathFinder->getShortcutPageNum($path);

// usage with all arguments
$array = $pagesPathFinder->getShortcutPageNum(&$path);
~~~~~

## Arguments

- `$path` `string`

## Return value

- `array` of [ pageNum, pageNumPrefix ]
